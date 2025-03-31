from Crypto.Cipher import AES
import base64
import os

# Generate a secure random key (16, 24, or 32 bytes for AES)
SECRET_KEY = os.urandom(32)  # 256-bit AES key

def pad(data):
    """
    Pads the input data to be a multiple of 16 bytes (AES block size).
    """
    padding_size = 16 - len(data) % 16
    return data + (chr(padding_size) * padding_size).encode()

def unpad(data):
    """
    Removes padding after decryption.
    """
    return data[:-ord(data[-1:])]

def encrypt_vote(vote_data):
    """
    Encrypts the vote data using AES encryption.
    """
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv=os.urandom(16))
    encrypted_data = cipher.encrypt(pad(vote_data.encode()))
    return base64.b64encode(cipher.iv + encrypted_data).decode('utf-8')

def decrypt_vote(encrypted_vote):
    """
    Decrypts the vote data.
    """
    encrypted_vote_bytes = base64.b64decode(encrypted_vote)
    iv = encrypted_vote_bytes[:16]  # Extract IV
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_vote_bytes[16:]))
    return decrypted_data.decode('utf-8')

# Example Usage
if __name__ == "__main__":
    vote = "Voter: user_123, Candidate: Candidate_A"
    encrypted = encrypt_vote(vote)
    print(f"Encrypted Vote: {encrypted}")

    decrypted = decrypt_vote(encrypted)
    print(f"Decrypted Vote: {decrypted}")
