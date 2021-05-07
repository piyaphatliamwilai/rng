import random

minimum = input("Give minimum number of random number generation you want -> ")
maximum = input("Give maximum number of random number generation you want -> ")

rng = random.random(minimum, maximum)

print(rng)
