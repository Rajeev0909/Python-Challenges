def common_divisible_numbers(numbers, factors1, factors2):
    set1 = {num for num in numbers if all(num % f == 0 for f in factors1)}
    set2 = {num for num in numbers if all(num % f == 0 for f in factors2)}
    return set1 & set2


numbers = range(1, 30)
factors1 = [2]
factors2 = [3]
print("Common Divisible Numbers:", common_divisible_numbers(numbers, factors1, factors2))
