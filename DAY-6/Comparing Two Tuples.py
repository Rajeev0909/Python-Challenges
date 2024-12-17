def compare_tuples(tup1, tup2):
    return all(a == b for a, b in zip(tup1, tup2))

# Test the function
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)
print("Are tuple1 and tuple2 equal?", compare_tuples(tuple1, tuple2))
print("Are tuple1 and tuple3 equal?", compare_tuples(tuple1, tuple3))
