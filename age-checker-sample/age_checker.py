# Check a person's age group and determine what they can do

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nHello, {name}! You are {age} years old.")

# Determine the age group
if age < 0:
    print("That's not a valid age!")
elif age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
    print("You can watch PG-13 movies.")
elif age < 65:
    print("You are an adult.")
    print("You can vote and drive.")
else:
    print("You are a senior citizen.")
    print("You may be eligible for senior discounts.")

# Check specific age milestones
if age >= 16:
    print("You are old enough to drive.")
if age >= 18:
    print("You are old enough to vote.")
if age >= 21:
    print("You are old enough to drink (in the US).")
