import random

numbers = random.sample(range(1, 1_000_000_001), 100_000)

with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(f"{number}\n")
