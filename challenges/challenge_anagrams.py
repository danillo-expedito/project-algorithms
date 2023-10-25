def merge_sort(string):
    """Faça o código aqui."""
    # Verify if string is empty
    if len(string) == 0:
        return ''

    # Lower case string and verify if string has only one character
    case_string = string.lower()
    if len(case_string) <= 1:
        return case_string

    # Split string in two parts
    mid = len(case_string) // 2
    left = case_string[:mid]
    right = case_string[mid:]

    # Recursive call
    left_half = merge_sort(left)
    right_half = merge_sort(right)

    # Merge
    sorted_string = ""
    i = j = 0
    # Compare left and right half indexes
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:  # If left index is lower than right,
            sorted_string += left_half[i]  # add left index to sorted string
            i += 1
        else:
            sorted_string += right_half[j]  # If right index is low/ than left,
            j += 1                          # add right index to sorted string

    # Add remaining indexes to sorted string
    sorted_string += left_half[i:]
    sorted_string += right_half[j:]

    return sorted_string


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    # Call merge_sort function to sort strings
    first_string_sorted = merge_sort(first_string)
    second_string_sorted = merge_sort(second_string)
    anagram = False

    # Verify if strings are anagrams
    if first_string_sorted == second_string_sorted:
        anagram = True
    # Verify if strings are empty
    if first_string_sorted == '' or second_string_sorted == '':
        anagram = False

    return (first_string_sorted, second_string_sorted, anagram)
