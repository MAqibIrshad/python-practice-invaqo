from iterables import natural_nums

natural_nums_iter = iter(natural_nums)

print(next(natural_nums_iter))  # Output: 1
print(next(natural_nums_iter))  # Output: 2
print(next(natural_nums_iter))  # Output: 3

print(natural_nums_iter.__next__())
print(natural_nums_iter.__iter__())