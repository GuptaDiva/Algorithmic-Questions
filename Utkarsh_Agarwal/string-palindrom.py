#write a program to check whether the string is palindrome of not(case-insensitive)
string = input("Input: ").lower()


# The expression `all(string[ind]==string[-1-ind] for ind in range(0,len(string)))` is checking if
# all characters in the string are equal to their corresponding characters from the end of the
# string.
if all(string[ind]==string[-1-ind] for ind in range(0,len(string))):# -ve index represents the index from last position
    print("Output: String is palindrome")
else:
    print ("Output: String is not palindrome ")