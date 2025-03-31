import hashlib
import random

# Simulated biometric data storage (In a real system, use a secure database)
registered_users = {
    "user_1": hashlib.sha256(b"fingerprint_123").hexdigest(),
    "user_2": hashlib.sha256(b"face_scan_456").hexdigest(),
}

def authenticate_user(user_id, biometric_data):
    """
    Simulates biometric authentication.

    :param user_id: Unique identifier for the user.
    :param biometric_data: The biometric data (e.g., fingerprint or face scan).
    :return: Boolean indicating whether authentication was successful.
    """
    try:
        hashed_data = hashlib.sha256(biometric_data.encode()).hexdigest()

        # Verify biometric data against stored records
        if user_id in registered_users and registered_users[user_id] == hashed_data:
            return True  # Authentication successful

        return False  # Authentication failed

    except Exception as e:
        print(f"Error in biometric authentication: {e}")
        return False
