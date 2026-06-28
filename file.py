from pathlib import Path

p = Path("data.txt")

print(p.exists())
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)