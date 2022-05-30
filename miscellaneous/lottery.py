import random
list = []
for i in range(100):
    list.append(random.randrange(1000000000, 9999999999))
winners = random.sample(list, 2)
print("Lucky 2 lottery tickets are", winners)