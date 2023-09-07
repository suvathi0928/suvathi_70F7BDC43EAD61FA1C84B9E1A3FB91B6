#implement a recursive function  to calculate the  factorial of  a  given number in python example.

def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: compute factorial by multiplying n with factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a value : "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
