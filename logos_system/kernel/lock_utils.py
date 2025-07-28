# subsystems/TETRAGNOS/lock_utils.py
from functools import wraps

def lock_required(func):
    """Block calls that do not pass a LockContext(token=…) keyword."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token")
        if token != "VALID":               # placeholder check
            raise PermissionError("Missing or invalid security token")
        return func(*args, **kwargs)
    return wrapper
