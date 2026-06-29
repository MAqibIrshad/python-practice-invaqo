try:
    x = int(input("Enter any number: "))
except ValueError:
    print("Invalid Number")
else:
    print(f"Valid: {x}")
finally:
    print(f"Value added Successfully finally")

class NegativeNumberError(Exception):
    pass

if x < 0:
    raise NegativeNumberError("Negative Values not allowed")