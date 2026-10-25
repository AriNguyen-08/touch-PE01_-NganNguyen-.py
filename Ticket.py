
# Movie theater ticket prices

while True:
    # Ask the user to enter their age
    age = int(input("How old are you? "))

    # Check the ticket price based on age
    if age < 0:
        print("Please enter a valid age.")

    elif age < 3:
        print("Your movie ticket is free.")

    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")

    else:
        print("Your movie ticket costs $15.")

    # Ask if the user wants to continue
    again = input("Do you want to check another ticket? (yes/no): ")

    if again.lower() == "no":
        print("Thank you! Goodbye!")
        break
