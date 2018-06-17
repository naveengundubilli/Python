import sys

def Factorial(n): # return factorial
    result = 1
    for i in range (1,n):
        result = result * i
    return result

print("factorial is ",Factorial(10))