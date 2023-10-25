def find_duplicate(nums):
    """Faça o código aqui."""
    # Verify if nums is a list, if it is not, return False
    if nums is None or isinstance(nums, str) or len(nums) == 1:
        return False

    # Sort the list and create a set to store the numbers
    nums.sort()
    duplicate = set()

    for num in nums:
        if not isinstance(num, int) or num < 0:  # Verify if the list has only
            return False                         # positive integers
        if num in duplicate:  # Verify if the number is already in the set
            return num        # If it is, return the number
        duplicate.add(num)    # If it is not, add the number to the set
    return False
