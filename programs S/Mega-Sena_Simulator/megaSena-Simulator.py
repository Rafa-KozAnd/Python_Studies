import random

randomNumber = [
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60)
]

randomNumber01 = sorted(random.sample(range (1,61), 6))
randomNumber02 = sorted(random.sample(range (1,61), 6))
randomNumber03 = sorted(random.sample(range (1,61), 6))
randomNumber04 = sorted(random.sample(range (1,61), 6))
randomNumber05 = sorted(random.sample(range (1,61), 6))
randomNumber06 = sorted(random.sample(range (1,61), 6))

print("\n1° Sequência de números: ", *randomNumber01)
print("\n2° Sequência de números: ", *randomNumber02)
print("\n3° Sequência de números: ", *randomNumber03)
print("\n4° Sequência de números: ", *randomNumber04)
print("\n5° Sequência de números: ", *randomNumber05)
print("\n6° Sequência de números: ", *randomNumber06)
print("\n")