from flask import request, jsonify
import re

def validate_input(data):
    """
    Kiểm tra input có hợp lệ không (chỉ chứa chữ và số)
    """
    pattern = re.compile("^[a-zA-Z0-9_]*$")
    if not pattern.match(data):
        return False
    return True

def security_check(func):
    def wrapper(*args, **kwargs):
        data = request.json
        if 'action' in data and not validate_input(data['action']):
            return jsonify({"status": "error", "message": "Invalid input"}), 400
        return func(*args, **kwargs)
    return wrapper
