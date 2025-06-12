from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chatbot import generate_response
import os

# Only ONE app instance
app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app)


@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    message = data.get("message", "")
    response = generate_response(message)
    return jsonify({"response": response})

@app.route('/')
def index():
    return jsonify({'status': 'EmpathyAI API is running.'})




# app = Flask(__name__, static_folder='build', static_url_path='')

@app.route('/home')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')

    # Serve static files (JS/CSS)
@app.route('/build/static/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)
