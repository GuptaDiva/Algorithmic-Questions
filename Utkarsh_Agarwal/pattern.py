#Write a program to print the following pattern:
# Output:
#      *
#     **
#    ***
#   ****
#  *****

for i in range(5):
    for k in range(4,i,-1):
        print(' ', end=" ")
    # The line `for j in range(i+1):` is used to iterate `j` from 0 to `i` (inclusive). This is used
    # to print the appropriate number of asterisks (`*`) in each row of the pattern.
    for j in range(i+1):
        print('*',end=' ')
    print()