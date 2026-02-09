import random

random_int = random.randint(1,10)
print(random_int)

random_float = random.uniform(1,6)
print(random_float)

random_num_0_to_10 = random.random() *10
print(random_num_0_to_10)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")