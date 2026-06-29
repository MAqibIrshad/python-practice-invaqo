def sum(X:int, y:int):
    print(f"Sum: {X+y}")

sum(5,6)

def greatest(*args:int):
    a, b, c, d = args
    items_list = [value for value in args]
    largest = args[0]
    for i in range(0, len(args)):
        print(args[i])
        if args[i] > largest:
            largest = args[i]
        
    return largest, items_list

print(greatest(1, 2, 3 ,4))

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not exists")


text = "MuhammadAqibIrshad"
print(text[-5:])


for i in range(1, 10):
    if i == 5:
        break;
    print(i)






        