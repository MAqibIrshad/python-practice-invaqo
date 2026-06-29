from itertools import count, chain, combinations

for i in count(5):
    print(f"Num iterated: {i}")
    if i == 10:
        break

list_1 = [101, 102, 103]
list_2 = ["Aqib", "Adil", "Haadi"]
list_3 = ["CS", "3D", "IT"]

for item in chain(list_1, list_2, list_3):
    print(item)

list_4 = ["A", "B", "C"]
print(list(combinations(list_4, 2)))