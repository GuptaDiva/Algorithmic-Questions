# Remove duplicates from a sorted array of positive numbers and return the remaining array, 
# with the unique elements put towards the starting of the array, it doesn't matter what 
# you put after the unique elements in the array.
# Input: nums = [1,1,1,2,3,4]
# Output: nums = [1,2,3,4,-1,-1]
nums = []
# The `try:` block is used to enclose a section of code that may potentially raise an exception. In
# this case, it is used to handle any `ValueError` exceptions that may occur when converting user
# input to integers.
try:
    n = int(input("Enter the number of integers to be input: "))
    # Get the integers from the user
    for i in range(0, n):
        num = int(input("Enter an +ve integer: "))
        nums.append(num)
# The `except ValueError:` block is used to handle any `ValueError` exceptions that may occur during
# the execution of the code.
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit(1)
unique_nums = []
# Iterate through the original list
for num in nums:
    # If the element is not already in unique_nums, add it
    if num not in unique_nums:
        unique_nums.append(num)
for _ in range(n-len(unique_nums)):
    unique_nums.append(-1)
# Now, unique_nums contains the unique elements from nums
print(unique_nums)