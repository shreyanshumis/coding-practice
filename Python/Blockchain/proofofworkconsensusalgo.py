import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.proof = 0

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        genesis_block.proof = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, previous_block.compute_hash())
        new_block.proof = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block):
        block.proof = 0
        while not block.compute_hash().startswith("0" * self.difficulty):
            block.proof += 1
        return block.proof

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.compute_hash() != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.compute_hash():
                return False
            if not current_block.compute_hash().startswith("0" * self.difficulty):
                return False

        return True

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)

    print("Mining Block 1...")
    blockchain.add_block("Transaction Data 1")

    print("Mining Block 2...")
    blockchain.add_block("Transaction Data 2")

    print("Blockchain Valid:", blockchain.is_chain_valid())

    for block in blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Proof: {block.proof}")
        print(f"Hash: {block.compute_hash()}")
        print("-" * 50)
