# Define a reusable function
def greet_user(name):
    print(f"Welcome, {name}!")

# First place where the function is used
user_name = input("Please enter your name: ")
greet_user(user_name)  # Calling the function here

# Another place where the function is used again
friend_name = "Alice"
greet_user(friend_name)  # Calling the same function again with a different name
