import random
list = [1, 2, 3, 4, 5, 6, 7, 8]
sans = []
for i in range(30):
    aa = random.choice(list)
    sans.append(aa)
print(sans)

print({i: sans.count(i) for i in sans})
