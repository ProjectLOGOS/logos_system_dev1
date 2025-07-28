# thonoc_nexus.py
"""
ThonocNexus: Master orchestrator for the THŌNOC subsystem.
Dispatches queries to Core API, BayesianNexus, FractalNexus, and ForecastingNexus,
aggregates results into a unified report.
Place this file at your project root (e.g. THONOC1/thonoc_nexus.py).
"""
import json
import traceback
from typing import Any, Dict, List, Optional

# Import toolkit-level and core orchestrators
from core.thonoc_core_API import ThonocCoreAPI
from bayesian_predictor.bayesian_nexus import BayesianNexus
from fractal_orbital.fractal_nexus import FractalNexus
from forecasting.forecasting_nexus import ForecastingNexus

class ThonocNexus:
    def __init__(self,
                 bayes_priors: str = 'config/bayes_priors.json',
                 fractal_priors: str = 'config/bayes_priors.json',
                 core_config: Optional[str] = None):
        # Core API (core logic + modal + translation)
        self.core_api   = ThonocCoreAPI(config_path=core_config)
        # Toolkit-level nexuses
        self.bayes_nexus      = BayesianNexus(priors_path=bayes_priors)
        self.fractal_nexus    = FractalNexus(fractal_priors)
        self.forecasting_nexus = ForecastingNexus()

    def run(self, query: str, series: Optional[List[float]] = None) -> Dict[str, Any]:
        report: Dict[str, Any] = {
            'query': query,
            'core': None,
            'bayesian': None,
            'fractal': None,
            'forecasting': None,
            'errors': {}
        }
        # 1) Core run
        try:
            report['core'] = self.core_api.run(query)
        except Exception:
            report['errors']['core'] = traceback.format_exc()

        # 2) Bayesian pipeline
        try:
            report['bayesian'] = self.bayes_nexus.run_pipeline(query)
        except Exception:
            report['errors']['bayesian'] = traceback.format_exc()

        # 3) Fractal pipeline (use first 3 words as keywords)
        keywords: List[str] = query.split()[:3]
        try:
            report['fractal'] = self.fractal_nexus.run_pipeline(keywords)
        except Exception:
            report['errors']['fractal'] = traceback.format_exc()

        # 4) Forecasting pipeline (if series data provided)
        if series is not None:
            try:
                report['forecasting'] = self.forecasting_nexus.run_pipeline(series)
            except Exception:
                report['errors']['forecasting'] = traceback.format_exc()

        return report

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Thonoc Master Nexus')
    parser.add_argument('--query', required=True, help='Input natural-language query')
    parser.add_argument('--series', nargs='+', type=float,
                        help='Optional time series data for forecasting')
    parser.add_argument('--core-config', help='Path to core JSON config')
    parser.add_argument('--bayes-priors', default='config/bayes_priors.json', help='Bayesian priors JSON')
    parser.add_argument('--fractal-priors', default='config/bayes_priors.json', help='Fractal priors JSON')
    args = parser.parse_args()

    nexus = ThonocNexus(
        bayes_priors=args.bayes_priors,
        fractal_priors=args.fractal_priors,
        core_config=args.core_config
    )
    result = nexus.run(args.query, series=args.series)
    print(json.dumps(result, indent=2))
    with open('thonoc_nexus_report.json', 'w') as f:
        json.dump(result, f, indent=2)
