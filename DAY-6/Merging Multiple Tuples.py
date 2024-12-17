def merge_tuples(*tuples):
    return sum(tuples, ())

# Test the function
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = (6, 7, 8)
print("Merged Tuple:", merge_tuples(tuple1, tuple2, tuple3))
