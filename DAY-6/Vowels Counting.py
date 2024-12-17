def count_vowels(tup):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in tup if char.lower() in vowels)

# Test the function
chars = ('a', 'b', 'c', 'e', 'i', 'o', 'u', 'x', 'y')
print("Number of vowels:", count_vowels(chars))
