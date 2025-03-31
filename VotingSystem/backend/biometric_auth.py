import cv2  # OpenCV for image processing
import numpy as np
import os

# Assuming the stored biometric data is a template image (e.g., fingerprint template).
# The template will be stored after the user registers their fingerprint.

def store_biometric_data(user_id, fingerprint_image):
    """
    Save the biometric (fingerprint) image to the database or file system for future comparison.
    Here, we're saving it as a simple file.
    """
    file_path = f"biometrics/{user_id}.png"
    cv2.imwrite(file_path, fingerprint_image)
    return file_path


def authenticate_user(fingerprint_image):
    """
    Authenticate the user by comparing the input fingerprint image with stored biometric data.
    If matched, return authentication success.
    """
    # Assuming that the user ID or a unique identifier is provided.
    user_id = "user123"  # This should be dynamic in a real scenario
    
    # Load the stored biometric (fingerprint) template.
    stored_image_path = f"biometrics/{user_id}.png"
    
    if not os.path.exists(stored_image_path):
        return {"status": "failure", "message": "User biometric not registered."}

    stored_image = cv2.imread(stored_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Convert the input image to grayscale for comparison.
    input_image_gray = cv2.cvtColor(fingerprint_image, cv2.COLOR_BGR2GRAY)
    
    # Use template matching to compare the images.
    # (This is a basic method and not the most advanced, use specialized algorithms for more accurate matching.)
    result = cv2.matchTemplate(input_image_gray, stored_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9  # You can adjust this threshold based on the accuracy needed.
    
    if np.max(result) >= threshold:
        return {"status": "success", "message": "User authenticated successfully."}
    else:
        return {"status": "failure", "message": "Authentication failed."}
