
with open("data.txt", "r") as f:
    text = f.read()
    print(text)

from pathlib import Path

path = Path("data.txt")
print(path.exists())
print(path.name)
print(path.parent)

path.write_text("I have studied BSCS from MUL")

new_text = path.read_text()

print(new_text)
