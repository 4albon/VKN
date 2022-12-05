import cube 

def dil(a,b):
    del_a = []
    del_b = []
    res = []
    for i in range(1,a,1):
        if a % i == 0:
            del_a.append(i)
            
    for i in range(1,b,1):
        if b % i == 0:
            del_b.append(i)
            
    if del_a < del_b:
        for i in del_a:
            if i in del_b:
                res.append(i)
    else:
        for i in del_b:
            if i in del_a:
                res.append(i)
            
    print(res)
    
def krat(n,a):
    res=[]
    
    for i in range(2,n+2,1):
        res.append(a*i)
    
    print(res)

dil(20,10)
krat(5, 4)

print(cube.v(4))
print(cube.s(4))