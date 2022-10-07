s = input(" Enter a string with characters: ")

dic = {}
for i in s.lower():
    dic[i] = dic.setdefault(i, 0) + 1
 
print('\n'.join([f'{it[0]} {it[1]} {s.lower().count(it[0]) / len(s) * 100}'
     for it in sorted(dic.items(), key=lambda x: x[1], reverse=True)]))