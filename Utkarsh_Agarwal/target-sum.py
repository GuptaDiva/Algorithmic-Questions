#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = []
try:
    n = int(input("Enter the number of integers to be input: "))
    # Get the integers from the user
    for i in range(0, n):
        num = int(input("Enter an integer: "))
        nums.append(num)
    target = int(input("Enter the target integer: "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit(1)

for index in range(len(nums)):
    for next_index in range(index + 1, len(nums)):
        if nums[index] + nums[next_index] == target:
            print(f"[{index}, {next_index}]")
