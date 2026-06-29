items = [1, 2, 3, 4 ,5]

it = iter(items)

print(it.__next__())
for i in range(len(items)):
    if(i == 4):
        break
    print(it.__next__())