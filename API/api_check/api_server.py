from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import generate_response

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    message = data.get("message", "")
    response = generate_response(message)
    return jsonify({"response": response})

@app.route('/')
def index():
    return jsonify({'status': 'EmpathyAI API is running.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


