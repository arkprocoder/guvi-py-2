'''write a program which is going to print the tables
if i give input as 5

5 x 1 =5
5 x 2 =10
---
5 x 10 =50 
'''
n=int(input("Enter the table number which you want to print:\n"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i} ")