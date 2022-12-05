

def shifr(mes):
    arr = list(mes)
    for i in range(0,len(arr),2):
        try:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        except:
            pass
    res = ''.join(arr)
    return res

print(shifr('ehllhop'))