str = input()

dict = {}
for i in str:
    if i.isalpha():
        i = i.lower()
        num  = dict.get(i,'0')
        dict[i] = int(num)+1

print(dict)