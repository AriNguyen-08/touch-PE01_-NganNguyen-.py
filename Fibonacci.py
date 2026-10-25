
# Function to generate Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num

# Ask the user how many numbers to generate
num = int(input("How many Fibonacci numbers do you want? "))

# Check if the input is valid
if num > 0:
    fibonacci(num)
else:
    print("Please enter a positive number.")
