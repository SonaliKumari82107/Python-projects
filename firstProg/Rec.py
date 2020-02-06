def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
        return fac
def factorial_recursive(n) :
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number=int(input("enter the number:"))
print("Factorial Using Iterative Method",factorial_iterative(number))
print("Factorial Using Recursive Method",factorial_recursive(number))
print("Fibonacci Series",fibonacci(number))