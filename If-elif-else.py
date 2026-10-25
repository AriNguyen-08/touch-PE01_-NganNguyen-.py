age = int(input("How old are you? "))

if age < 0:
    print("Please enter a valid age.")
elif 0 <= age < 2:
    print("You are a baby.")
elif 2 <= age < 4:
    print("You are a toddler.")
elif 4 <= age < 13:
    print("You are a kid.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")