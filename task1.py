# Define a function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Take input from the user
number = int(input("Enter a number: "))

# Call the function and display the result
result = factorial(number)
print(f"Factorial of {number} is: {result}")