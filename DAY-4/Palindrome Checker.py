def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if string is equal to its reverse

# Test the function
test_string = "A man a plan a canal Panama"
print(f"'{test_string}' is a palindrome:", is_palindrome(test_string))
