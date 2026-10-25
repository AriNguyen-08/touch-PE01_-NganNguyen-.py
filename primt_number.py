
# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is greater than 1
if num > 1:
    # Assume the number is prime
    is_prime = True

    # Check if the number can be divided by other numbers
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break

    # Print the result
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
else:
    print(f"{num} is not a prime number")

