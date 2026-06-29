
temp = float(input("Enter Temperature in Celsius: "))
farenheit = (temp * 9/5) + 32
print(f"{temp}°C is equal to {farenheit}°F")

import random
secret = random.randint(1, 10)
guess = None

while guess != secret:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Congratulations!")


