
with open("data.txt", "r") as f:
    text = f.read()
    print(text)

with open("data.txt", "a") as f:
    text_to_write = "I have learned from udemy"
    f.write(text_to_write)

with open("data.txt", "r") as f:
    read = f.read()
    print(read)
    
from contextlib import contextmanager

@contextmanager
def message():
    print(f"Start")
    yield
    print(f"Completed Successfully!")

with message():
    print(f"Processing.....")