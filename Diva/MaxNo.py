##To find the kth maximum number in an array.
lst=[]
len=int(input("Enter the length of the array.\n"))
for i in range(0,len):
    e=input("Enter the element.\n")
    lst.append(e)
k=int(input("Enter the value of k\n"))
lst.sort(reverse=True)
f=k-1
print(lst[f])
