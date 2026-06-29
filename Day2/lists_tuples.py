from func import tuple_to_dict
from func import unpack_tuple_5


days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days_of_week[-1])

days_of_week[0] = "NODAY"
print(days_of_week)


for idx, item in enumerate(days_of_week):
    a_dict = {idx, item}
    print(a_dict)


natural_nbrs = (1, 2, 3, 4, 5)

list_of_tuple = [x*2 for x in natural_nbrs]
print(list_of_tuple)

by_len = {w: len(w) for w in days_of_week}

print(by_len)

a = (1, 2, 3, 4, 5, 6)

result = list(map(lambda a: a*a,a ))
print(result)

print(tuple_to_dict(natural_nbrs))

print(unpack_tuple_5(natural_nbrs))