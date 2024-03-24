import random

sākums = input(f"Gribi 50 vai 100 ciparus?")
if sākums == "50": 
    random_numbers = [random.randint(1, 50) for _ in range(5)] 
    secība = sorted(random_numbers)
elif sākums == "100": 
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    secība = sorted(random_numbers)
print(secība)
