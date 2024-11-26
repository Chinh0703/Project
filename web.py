import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cấu hình logger để ghi vào file app.log
logging.basicConfig(
    level=logging.INFO,  # Mức độ log là INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Định dạng log
    handlers=[
        logging.FileHandler('app.log'),  # Ghi log vào file app.log
        logging.StreamHandler()  # In log ra console (tuỳ chọn)
    ]
)

# Route nhận dữ liệu từ frontend khi mở/đóng chatbox
@app.route('/toggle-chat', methods=['POST'])
def toggle_chat():
    data = request.get_json()  # Nhận dữ liệu JSON
    action = data.get('action')  # Lấy thông tin hành động (open/close)
    
    # Ghi log vào app.log
    app.logger.info(f"Chatbot action: {action}")
    
    return jsonify({"status": "success", "action": action})

# Route nhận dữ liệu thời gian thực thi của chatbot
@app.route('/log-performance', methods=['POST'])
def log_performance():
    data = request.get_json()  # Nhận dữ liệu JSON từ frontend
    execution_time = data.get('executionTime')  # Lấy thời gian thực thi từ frontend
    
    # Ghi log thời gian thực thi vào app.log
    app.logger.info(f"Chatbot performance time: {execution_time} ms")
    
    # Trả về kết quả cho client (frontend)
    return jsonify({"status": "success", "executionTime": execution_time})

if __name__ == '__main__':
    app.run(debug=True)