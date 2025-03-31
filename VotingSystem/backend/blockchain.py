import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mines the block by finding a hash with the required difficulty.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (Genesis block).
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain after mining.
        """
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, time.time(), data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain integrity.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False  # The block's hash has been altered

            if current_block.previous_hash != previous_block.hash:
                return False  # The chain link is broken

        return True


# Simulating the voting process
def cast_vote(voter_id, candidate):
    """
    Casts a vote by adding a new block to the blockchain.
    """
    global voting_blockchain
    vote_data = {"voter_id": voter_id, "candidate": candidate}
    voting_blockchain.add_block(vote_data)
    return voting_blockchain.get_latest_block().hash


# Initialize the blockchain for voting
voting_blockchain = Blockchain(difficulty=3)
