def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    # Base case (kinda)
    if len(word) == 0:
        return False
    # Compare the first and last index
    elif low_index >= high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    # recursive case that moves the indexes to compare the next letters
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
