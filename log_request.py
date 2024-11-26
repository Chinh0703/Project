import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Định nghĩa decorator log_request
def log_request(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Request received for {func.__name__} with arguments: {args}, {kwargs}")
        
        result = func(*args, **kwargs)
        
        logging.info(f"Response from {func.__name__}: {result}")
        
        return result
    return wrapper