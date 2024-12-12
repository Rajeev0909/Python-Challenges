user_string = input("Enter a string: ")

user_list = input("Enter a list of items : ").split(",")
user_list = [item.strip() for item in user_list]  # Clean up whitespace

user_tuple = tuple(input("Enter a tuple of items : ").split(","))

user_int = int(input("Enter an integer: "))
user_float = float(input("Enter a float: "))

# Display the types and values of the inputs
print("\n--- Data Types and Values ---")
print(f"The string is: '{user_string}' (Type: {type(user_string).__name__})")
print(f"The list is: {user_list} (Type: {type(user_list).__name__})")
print(f"The tuple is: {user_tuple} (Type: {type(user_tuple).__name__})")
print(f"The integer is: {user_int} (Type: {type(user_int).__name__})")
print(f"The float is: {user_float} (Type: {type(user_float).__name__})")
