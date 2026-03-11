import hashlib
import time
import matplotlib.pyplot as plt

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

def calculate_hash(index, previous_hash, timestamp, data, nonce, algorithm):
    value = f"{index}{previous_hash}{timestamp}{data}{nonce}"
    if algorithm == "sha256":
        return hashlib.sha256(value.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(value.encode()).hexdigest()
    elif algorithm == "md5":
        return hashlib.md5(value.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing algorithm!")

def proof_of_work(previous_block, data, difficulty, algorithm):
    index = previous_block.index + 1
    timestamp = time.time()
    nonce = 0

    start_time = time.time()
    while True:
        new_hash = calculate_hash(index, previous_block.hash, timestamp, data, nonce, algorithm)
        if new_hash.startswith(difficulty):
            break
        nonce += 1
    end_time = time.time()
    return Block(index, previous_block.hash, timestamp, data, new_hash, nonce), end_time - start_time

def run_experiments(difficulties, algorithms, data_samples):
    results = []
    
    genesis_block = Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block", 0, "sha256"), 0)
    
    for difficulty in difficulties:
        for algorithm in algorithms:
            for data in data_samples:
                new_block, time_taken = proof_of_work(genesis_block, data, difficulty, algorithm)
                results.append((difficulty, algorithm, data, time_taken))
                print(f"Difficulty: {difficulty}, Algorithm: {algorithm}, Data: {data}, Time: {time_taken:.4f}s")
    
    return results

def plot_results(results):
    labels = [f"{difficulty}-{algorithm}-{data}" for difficulty, algorithm, data, _ in results]
    times = [time_taken for _, _, _, time_taken in results]

    plt.figure(figsize=(10, 6))
    plt.barh(labels, times, color='green')
    plt.xlabel('Time (seconds)')
    plt.title('Proof of Work Time Comparison')
    plt.tight_layout()
    plt.show()

difficulties = ["0000", "00000", "AAAA", "9999"]
algorithms = ["sha256", "sha1", "md5"]
data_samples = ["Test", "Data", "12345"]

results = run_experiments(difficulties, algorithms, data_samples)
plot_results(results)


# #------Question------

# Extend /  save the exisiting program to convert it into Proof-of-Work consensus implementation.
# Check the time required to generate the correct nounce for each of the follwoing:

# 1) Use different hashing functions from hashlib
# 2) (Change the data and see the result) Store different type of dat like numbers, strings, different lengh of string etc.
# 3) print the time required to generate the nounce with leading 0000.
# 4) Change the leading character from "0000" to "9999" /  "AAAA".
# 5) also compare the time requried from "0000" to "00000".
# Generte a bar chart for the time required in different cases when the values are changed.