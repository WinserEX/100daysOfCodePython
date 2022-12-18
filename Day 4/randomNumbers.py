import random 
import my_module

rand_int = random.randint(1,10)

print(rand_int)

print(my_module.pi)

random_float = random.random()

print(random_float)

random_float1_5 = random.random()

print(random_float1_5 * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score} out of a 100")

dice = print(random.randint(1,6))

coinSide = random.randint(1,2)

if coinSide == 1:
    print("It's heads")
else:
    print("It's tails")
