dict = {}
for i in range(0, 5):
    str = input()
    l = str.split(' ')
    dict[(l[0],l[1])] = [l[2]+l[3],l[4],l[5]]

print(dict)

