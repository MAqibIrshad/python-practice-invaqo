def tuple_to_dict(tup:tuple):
    for idx, item in enumerate(tup):
        print(
            {
                idx: item
            }
        )

def unpack_tuple_5(tup:tuple):
    a, b, c, d, e = tup
    print(a,b,c,d,e)
