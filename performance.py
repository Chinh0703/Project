import time
from log_config import log_info

def measure_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Tính thời gian thực hiện (milliseconds)
        log_info(f"Function {func.__name__} executed in {execution_time:.2f}ms")
        return result
    return wrapper
