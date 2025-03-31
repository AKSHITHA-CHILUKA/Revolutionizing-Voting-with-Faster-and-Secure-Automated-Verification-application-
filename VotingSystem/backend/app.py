from flask import Flask, request, jsonify
import os
import joblib
from biometric_auth import authenticate_user  # Import your biometric authentication function
from blockchain import cast_vote  # Blockchain voting function
from encryption import encrypt_vote  # Encryption for vote
from ai_fraud_detection import detect_fraud  # Fraud detection in the voting process

app = Flask(__name__)

# Config for file upload
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "Welcome to the Secure Voting System API!"

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if 'biometric_data' not in request.files:
        return jsonify({"error": "No biometric data provided"}), 400
    
    biometric_data = request.files['biometric_data']
    
    # Save the file (you can do further processing like checking the file)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], biometric_data.filename)
    biometric_data.save(file_path)

    # Perform biometric authentication
    authentication_result = authenticate_user(file_path)
    if authentication_result['status'] == 'success':
        return jsonify({"status": "User authenticated successfully"}), 200
    else:
        return jsonify({"error": "Authentication failed"}), 401

@app.route('/cast_vote', methods=['POST'])
def vote():
    data = request.json
    if not data or not data.get('vote'):
        return jsonify({"error": "No vote data provided!"}), 400
    
    # Encrypt the vote
    encrypted_vote = encrypt_vote(data['vote'])
    
    # Detect fraud (Optional)
    fraud_detected = detect_fraud(encrypted_vote)
    if fraud_detected:
        return jsonify({"error": "Fraudulent voting attempt detected!"}), 403
    
    # Cast the vote using blockchain
    vote_status = cast_vote(encrypted_vote)
    if vote_status['status'] == 'success':
        return jsonify({"status": "Vote successfully casted!"}), 200
    else:
        return jsonify({"error": "Vote casting failed"}), 500

if __name__ == '__main__':
    # Ensure upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True)
