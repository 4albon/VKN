
res1 = 0
res2 = 0
res3 = 0

a = ['A', 'E', 'I', 'O', 'U', 'Y']
b = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
nums = ['1', '2', '3', '4', '5', '6', '7','8','9','0']

f=open('story.txt','r')
for line in f:
    for el in line:
        if el.upper() in a:
            res1 += 1
        elif el.upper() in b:
            res2 += 1
        elif el in nums:
            res3 += 1
            
print(res1,res2,res3)

