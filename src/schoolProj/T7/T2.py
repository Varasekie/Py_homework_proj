import random
l1 = []
l2 = []
for i in range(0,20):
    l1.append(random.randint(10,100))

l11 = sorted(l1[:10])
l12 = sorted(l1[11:],reverse=True)
l11.extend(l12)
print(l11)
