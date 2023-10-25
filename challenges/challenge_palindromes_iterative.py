def is_palindrome_iterative(word):
    """Faça o código aqui."""
    # Verify if the word is empty
    if len(word) == 0:
        return False
    # Declare the indexes
    low_index = 0
    high_index = len(word) - 1

    # Compare the first and last index and
    # move the indexes to compare the next letters
    while low_index < high_index:
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1
    # If the word is a palindrome, return True
    return True
