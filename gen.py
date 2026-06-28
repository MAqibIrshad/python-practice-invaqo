

natural_nums_iter = iter([1, 2, 3, 4, 5])
print(type(natural_nums_iter))

def printer(nums:list):
    for num in nums:
        yield num
    return print(f"Finally: {num}")

gen = printer(natural_nums_iter)
print(type(gen))

for x in gen:
    print(x)


