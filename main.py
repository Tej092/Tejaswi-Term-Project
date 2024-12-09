import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash or self.chain[-1].hash,
            timestamp=time.time(),
            data=self.current_transactions,
            hash=self.hash_block(proof, previous_hash)
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block.index + 1

    def hash_block(self, proof, previous_hash):
        return hashlib.sha256(f'{proof}{previous_hash}'.encode('utf-8')).hexdigest()

    def validate_transaction(self, sender, recipient, amount):
        if amount <= 0:
            return False
        if sender == recipient:
            return False
        return True

    @property
    def last_block(self):
        return self.chain[-1]

    def run(self):
        # Creating a few sample transactions
        self.new_transaction('user1', 'user2', 10)
        self.new_transaction('user2', 'user3', 5)
        self.new_block(proof=1234, previous_hash='abc')

        # Printing the blockchain
        for block in self.chain:
            print(f'Block {block.index}: {block.data} - Hash: {block.hash}')

if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.run()