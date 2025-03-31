from cryptography.fernet import Fernet

# Generate a key for encryption (in production, you should store it securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt the vote
def encrypt_vote(vote):
    encrypted_vote = cipher_suite.encrypt(vote.encode())
    return encrypted_vote
