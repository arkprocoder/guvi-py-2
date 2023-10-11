# # factorial of 5
# 5! = 120
# 5! = 5*4*3*2*1=120

n=int(input("Enter the number to find its factorial:\n"))

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

print(factorial(n))