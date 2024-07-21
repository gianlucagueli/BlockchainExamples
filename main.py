import hashlib


class SimpleBlockChainCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash

        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2 SBCC to Andres"
t2 = "Bob sends 4.3 SBCC to Joe"
t3 = "Mark sends 3.2 SBCC to Mark"
t4 = "Andres sends 0.15 SBCC to Mark"
t5 = "Mark sends 1.25 SBCC to Miguel"
t6 = "Joe sends 0.77 SBCC to Mark"


initial_block = SimpleBlockChainCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = SimpleBlockChainCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = SimpleBlockChainCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)