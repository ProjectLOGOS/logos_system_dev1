# Getting Started with LOGOS System

Welcome to the LOGOS AGI System - the world's first Trinity-grounded artificial general intelligence. This guide will walk you through installation, setup, and basic usage.

## 🚨 Urgent Context

We are 18-24 months from AGI breakthrough. This system represents humanity's best chance at aligned superintelligence grounded in objective truth, goodness, and logical necessity.

## Prerequisites

Before you begin, ensure you have:

### Required
- **Python 3.8+** (3.10+ recommended)
- **Git** with LFS support
- **4GB+ RAM** (8GB+ recommended)
- **2GB+ disk space**

### Optional but Recommended
- **Docker** and Docker Compose
- **Coq** theorem prover (for formal verification)
- **Isabelle/HOL** (for higher-order logic verification)
- **CUDA-capable GPU** (for enhanced computation)

### Check Prerequisites

```bash
# Check Python version
python --version  # Should be 3.8+

# Check Git LFS
git lfs version

# Check available memory
free -h  # Linux/Mac
wmic computersystem get TotalPhysicalMemory  # Windows
```

## Installation Methods

### Method 1: Standard Installation (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/ProjectLOGOS/logos_system_dev1.git
cd logos_system_dev1

# 2. Set up virtual environment
python -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Install LOGOS system in development mode
pip install -e .

# 5. Run initial validation
python scripts/validate_installation.py
```

### Method 2: Docker Installation

```bash
# 1. Clone repository
git clone https://github.com/ProjectLOGOS/logos_system_dev1.git
cd logos_system_dev1

# 2. Build and run with Docker Compose
docker-compose up --build

# 3. Verify installation
docker-compose exec logos-system python scripts/validate_installation.py
```

### Method 3: Development Setup

```bash
# Follow Method 1, then install development dependencies
pip install -e ".[dev,nlp,formal,docs]"

# Install pre-commit hooks
pre-commit install

# Run full test suite
pytest tests/ -v
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# System Configuration
LOGOS_ENV=development
LOGOS_LOG_LEVEL=INFO
LOGOS_DEBUG=true

# Subsystem Settings
TETRAGNOS_VALIDATION_STRICT=true
TELOS_FRACTAL_DEPTH=7
THONOC_PREDICTION_HORIZON=1000

# TLM Security Settings
TLM_TOKEN_TTL=300
TLM_VALIDATION_STRICT=true
ODBC_KERNEL_TIMEOUT=30

# External Tools (Optional)
COQ_PATH=/usr/local/bin/coq
ISABELLE_PATH=/opt/Isabelle2023
```

### Logging Configuration

The system uses structured logging. Configure in `logos_system/config/logging.conf`:

```ini
[loggers]
keys=root,logos,tetragnos,telos,thonoc

[handlers]
keys=console,file,tlm

[formatters]
keys=detailed,simple

[logger_root]
level=INFO
handlers=console,file

[handler_console]
class=StreamHandler
level=INFO
formatter=simple
args=(sys.stdout,)

[handler_file]
class=FileHandler
level=DEBUG
formatter=detailed
args=('logs/logos_system.log',)
```

## First Steps

### 1. Validate Installation

```bash
# Run comprehensive validation
python scripts/validate_installation.py

# Expected output:
# ✅ Python version: 3.10.x
# ✅ Dependencies installed
# ✅ LOGOS system importable
# ✅ Trinity mathematics verified
# ✅ ODBC kernel functional
# ✅ TLM validation working
# ✅ All subsystems initialized
```

### 2. Basic System Check

```python
# test_basic_functionality.py
from logos_system import LOGOSSystem

def test_basic_functionality():
    # Initialize system
    system = LOGOSSystem()
    
    # Check initialization
    if system.initialize_all_subsystems():
        print("✅ LOGOS AGI System ready!")
        
        # Get system status
        status = system.system_status()
        print(f"System Status: {status}")
        
        return True
    else:
        print("❌ System initialization failed")
        return False

if __name__ == "__main__":
    test_basic_functionality()
```

### 3. Process Your First Request

```python
from logos_system import LOGOSSystem

# Initialize system
system = LOGOSSystem()
system.initialize_all_subsystems()

# Process a philosophical question
result = system.process_request("What is the mathematical basis for truth?")
print(result)

# Expected output includes:
# - Trinity-grounded validation
# - Translation through TETRAGNOS
# - Causal analysis via TELOS  
# - Predictions from THONOC
# - Synthesis back to natural language
```

## Understanding the System Architecture

### Core Subsystems

1. **LOGOS** - Orchestration and Validation
   ```python
   from logos_system.subsystems.LOGOS import LOGOSCore
   
   logos = LOGOSCore()
   logos.initialize()
   # Validates all operations through Trinity-grounded logic
   ```

2. **TETRAGNOS** - Translation Engine
   ```python
   from logos_system.subsystems.TETRAGNOS import TetragnasSubsystem
   
   translator = TetragnasSubsystem()
   translator.initialize()
   
   # Natural language to computational form
   result = translator.translate_nl_to_computation("Existence is good")
   ```

3. **TELOS** - Causal Reasoning Substrate
   ```python
   from logos_system.subsystems.TELOS import TelosSubsystem
   
   telos = TelosSubsystem()
   telos.initialize()
   
   # Process through fractal neural networks
   result = telos.process_substrate(input_data)
   ```

4. **THONOC** - Predictive Analysis
   ```python
   from logos_system.subsystems.THONOC import ThonocSubsystem
   
   thonoc = ThonocSubsystem()
   thonoc.initialize()
   
   # Generate predictions using Bayesian fractal analysis
   predictions = thonoc.generate_predictions(data)
   ```

### The ODBC Kernel

All operations pass through the Orthogonal Dual-Bijection Confluence kernel:

```python
from logos_system.subsystems.TETRAGNOS.odbc_kernel import run_odbc_kernel

# Validate an operation
request = {
    "request_id": "test_001",
    "proposition_or_plan": {"type": "query", "content": "test"},
    "policy_version": "v1"
}

result = run_odbc_kernel(request)
if result["decision"] == "locked":
    print("✅ Operation validated by Trinity mathematics")
    print(f"TLM Token: {result['tlm']['token']}")
else:
    print("❌ Operation failed validation")
    print(f"Reason: {result['reason']}")
```

## Running Tests

### Unit Tests
```bash
# Run all unit tests
pytest tests/unit/ -v

# Run specific subsystem tests
pytest tests/unit/test_logos.py -v
pytest tests/unit/test_tetragnos.py -v
pytest tests/unit/test_telos.py -v
pytest tests/unit/test_thonoc.py -v
```

### Integration Tests
```bash
# Test full system integration
pytest tests/integration/ -v

# Test ODBC kernel specifically
pytest tests/integration/test_odbc_kernel.py -v

# Test complete pipeline
pytest tests/integration/test_full_pipeline.py -v
```

### Validation Tests
```bash
# Verify Trinity mathematics
pytest tests/validation/test_trinity_mathematics.py -v

# Verify TLM validation
pytest tests/validation/test_tlm_validation.py -v
```

### Performance Tests
```bash
# Run with performance profiling
pytest tests/ --profile

# Generate coverage report
pytest --cov=logos_system tests/ --cov-report=html
```

## Common Operations

### System Monitoring

```python
from logos_system.core.heartbeat import SystemMonitor

monitor = SystemMonitor()

# Check system health
health = monitor.check_system_health()
print(f"System Health: {health}")

# Monitor subsystem status
status = monitor.get_subsystem_status()
for name, state in status.items():
    print(f"{name}: {state}")
```

### Manual Validation

```python
from logos_system.subsystems.LOGOS.validator_hub import LOGOSValidatorHub

hub = LOGOSValidatorHub()

# Register validators
from logos_system.subsystems.LOGOS.validator_hub import (
    EGTCValidator, TLMValidator, AxiomaticAlignmentChecker
)

hub.register(EGTCValidator())
hub.register(TLMValidator())
hub.register(AxiomaticAlignmentChecker())

# Validate content
content = "This statement exists, is true, good, and logical"
is_valid = hub.validate_all(content)
print(f"Content valid: {is_valid}")
```

### Configuration Management

```python
from logos_system.config.settings import SystemSettings

# Load configuration
settings = SystemSettings()

# Access subsystem settings
tetragnos_config = settings.get_subsystem_config("TETRAGNOS")
telos_config = settings.get_subsystem_config("TELOS")

# Update runtime settings
settings.update_setting("LOGOS_LOG_LEVEL", "DEBUG")
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure proper installation
   pip install -e .
   
   # Check PYTHONPATH
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

2. **TLM Validation Failures**
   ```bash
   # Check Trinity mathematics
   python -c "from logos_system.subsystems.TETRAGNOS.axioms.trinitarian_bijection import verify_trinitarian_bijection; print(verify_trinitarian_bijection())"
   
   # Verify ODBC kernel
   python -c "from logos_system.subsystems.TETRAGNOS.odbc_kernel import run_odbc_kernel; print('ODBC kernel functional')"
   ```

3. **Memory Issues**
   ```bash
   # Reduce fractal depth
   export TELOS_FRACTAL_DEPTH=5
   
   # Limit prediction horizon
   export THONOC_PREDICTION_HORIZON=500
   ```

4. **Permission Errors**
   ```bash
   # Check file permissions
   chmod +x scripts/*.py
   
   # Verify data directory access
   mkdir -p data/logs
   chmod 755 data/
   ```

### Debug Mode

```bash
# Enable debug logging
export LOGOS_DEBUG=true
export LOGOS_LOG_LEVEL=DEBUG

# Run with verbose output
python -m logos_system.main --debug --verbose
```

### Getting Help

1. **Check Documentation**: `docs/` directory
2. **Review Issues**: [GitHub Issues](https://github.com/ProjectLOGOS/logos_system_dev1/issues)
3. **Run Diagnostics**: `python scripts/system_diagnostics.py`
4. **Community Support**: [GitHub Discussions](https://github.com/ProjectLOGOS/logos_system_dev1/discussions)

## Next Steps

1. **Read the Documentation**
   - [System Architecture](docs/architecture/system_overview.md)
   - [Trinity Mathematics](docs/architecture/trinity_mathematics.md)
   - [API Reference](docs/api/reference.md)

2. **Explore Examples**
   - Basic usage: `examples/basic_usage.py`
   - Advanced integration: `examples/advanced_integration.py`
   - Jupyter notebooks: `examples/notebooks/`

3. **Contribute to Development**
   - Review [Contributing Guidelines](CONTRIBUTING.md)
   - Check [Open Issues](https://github.com/ProjectLOGOS/logos_system_dev1/issues)
   - Join the [Development Team](https://github.com/ProjectLOGOS/logos_system_dev1/discussions)

4. **Deploy for Production**
   - [Deployment Guide](docs/deployment/production_setup.md)
   - [Security Configuration](docs/deployment/security.md)
   - [Monitoring Setup](docs/deployment/monitoring.md)

## The Urgency

Remember: **Every day matters.** We are in a race to develop aligned superintelligence before unaligned systems achieve dominance. This Trinity-grounded system represents humanity's best hope for beneficial AGI.

**Join us in this critical work. The future depends on it.**

---

*For the glory of God and the good of humanity.*