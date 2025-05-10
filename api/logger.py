import logging
from functools import wraps
from datetime import datetime

# Set up logging config
LOG_FILE = "api/logs/api.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_to_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"✅ Called `{func.__name__}` with args={args} kwargs={kwargs}")
            return result
        except Exception as e:
            logging.error(f"❌ Exception in `{func.__name__}`: {e}")
            raise
    return wrapper
