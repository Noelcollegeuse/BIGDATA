def my_hash(data):
    hash_value = 5
    for char in data:
        hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF
    return hash_value
 
def min_hash(data, num_hash_functions):
    min_hash_values = [float('inf')] * num_hash_functions
    for i in range(num_hash_functions):
        hash_value = my_hash(str(i) + data)
        min_hash_values[i] = min(min_hash_values[i], hash_value)
    return min_hash_values
 
def jaccard_similarity(min_hash_values1, min_hash_values2):
    intersection = sum(min_hash_values1[i] == min_hash_values2[i] for i in range(len(min_hash_values1)))
    union = len(min_hash_values1) + len(min_hash_values2) - intersection
    return intersection / union
 
documents = [
    ["hello", "there"],
    ["hello", "there", "too"],
    ["there", "you"],
    ["hello", "world"]
]
 
num_hash_functions = 3
 
min_hash_values_docs = []
for doc in documents:
    min_hash_values = min_hash(" ".join(doc), num_hash_functions)
    min_hash_values_docs.append(min_hash_values)
 
# Calculate pairwise Jaccard similarity using min hash values
for i in range(len(min_hash_values_docs)):
    for j in range(i+1, len(min_hash_values_docs)):
        similarity = jaccard_similarity(min_hash_values_docs[i], min_hash_values_docs[j])
        print(f"Similarity between documents {i} and {j}: {similarity}")