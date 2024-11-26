import functools
import logging
from flask import request

# Thiết lập logging để ghi vào file 'app.log' và ra console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),   # Ghi vào file
        logging.StreamHandler()           # Ghi ra console
    ]
)

def log_action(func):
    """
    Decorator để log các request và response.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log thông tin request
        logging.info(f"Received request: {request.method} {request.path}")
        if request.json:
            logging.info(f"Request JSON data: {request.json}")

        # Gọi hàm chính
        response = func(*args, **kwargs)

        # Kiểm tra xem response có phải là một tuple không
        if isinstance(response, tuple):
            # Nếu là tuple, phần tử thứ hai là status_code
            status_code = response[1]
        else:
            # Nếu không, sử dụng status_code từ đối tượng response
            status_code = response.status_code

        # Log thông tin response
        logging.info(f"Response status: {status_code}")
        return response

    return wrapper