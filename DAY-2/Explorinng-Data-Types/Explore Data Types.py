# Prompt user for different data types
user_string = input("Enter a string: ")

user_list = input("Enter a list of items (comma-separated): ").split(",")
user_list = [item.strip() for item in user_list]  # Clean up whitespace

user_tuple = tuple(input("Enter a tuple of items (comma-separated): ").split(","))

user_int = int(input("Enter an integer: "))
user_float = float(input("Enter a float: "))

# Display the types and values of the inputs
print("\n--- Data Types and Values ---")
print(f"The string is: '{user_string}' (Type: {type(user_string).__name__})")
print(f"The list is: {user_list} (Type: {type(user_list).__name__})")
print(f"The tuple is: {user_tuple} (Type: {type(user_tuple).__name__})")
print(f"The integer is: {user_int} (Type: {type(user_int).__name__})")
print(f"The float is: {user_float} (Type: {type(user_float).__name__})")

# Additional operations on each data type
print("\n--- Additional Operations ---")
print(f"Length of the string: {len(user_string)}")
print(f"Length of the list: {len(user_list)}")
print(f"First item in the tuple: {user_tuple[0] if len(user_tuple) > 0 else 'Tuple is empty'}")
print(f"Square of the integer: {user_int ** 2}")
print(f"Float divided by 2: {user_float / 2}")
