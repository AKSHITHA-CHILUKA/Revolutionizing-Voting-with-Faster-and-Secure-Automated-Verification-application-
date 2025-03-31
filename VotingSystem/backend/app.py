from flask import Flask, request, jsonify, send_from_directory
import os
from biometric_auth import authenticate_user
from blockchain import cast_vote
from encryption import encrypt_vote
from ai_fraud_detection import detect_fraud

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return "Welcome to the Secure Voting System API"

# Route for serving favicon (to avoid 404 errors)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Route for User Authentication
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    user_id = data.get('user_id')
    biometric_data = data.get('biometric_data')

    if not user_id or not biometric_data:
        return jsonify({"error": "Missing user_id or biometric_data"}), 400

    authenticated = authenticate_user(user_id, biometric_data)

    if authenticated:
        return jsonify({"message": "User authenticated successfully"})
    else:
        return jsonify({"error": "Authentication failed"}), 401

# Route for Casting a Vote
@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    user_id = data.get('user_id')
    vote_choice = data.get('vote_choice')

    if not user_id or not vote_choice:
        return jsonify({"error": "Missing user_id or vote_choice"}), 400

    encrypted_vote = encrypt_vote(vote_choice)
    transaction_hash = cast_vote(user_id, encrypted_vote)

    return jsonify({
        "message": "Vote successfully casted",
        "transaction_hash": transaction_hash
    })

# Route for Fraud Detection
@app.route('/fraud-detection', methods=['POST'])
def fraud_detection():
    data = request.json
    transaction_data = data.get('transaction_data')

    if not transaction_data:
        return jsonify({"error": "Missing transaction data"}), 400

    fraud_detected = detect_fraud(transaction_data)

    return jsonify({
        "fraud_detected": fraud_detected
    })

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
