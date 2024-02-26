def shingle(text, shingle_size):
    """
    Generates overlapping sequences of words (shingles) from a given text.

    Args:
    text (str): The input text to generate shingles from.
    shingle_size (int): The size of the shingles to generate.

    Returns:
    list: A list of shingles generated from the input text.
    """

    # Tokenize the input text into words
    words = text.split()

    # Generate shingles of the specified size
    shingles = [words[i:i + shingle_size] for i in range(len(words) - shingle_size + 1)]
 
    return shingles
text = "Test data generation refers to the process of creating and maintaining values for testing with the intention of using it for testing purposes. It consists of creating synthetic or representative data to validate the functionality, performance, security, and various other aspects of the software"
print(text)
shingles = shingle(text,3)
print(shingles)
s = set(shingle(text,3))