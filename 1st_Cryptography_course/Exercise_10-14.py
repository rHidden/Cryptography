import random, time
current1 = time.time()
random.seed(current1)
r1 = random.randrange(0, 65534)

current2 = time.time()
random.seed(current1 + current2)
r2 = random.randrange(0, 65534)

print(r1)
print(r2)

for i in range(1000):
    print(random.randint(0,192))