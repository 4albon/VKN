import pandas as pd 
import numpy as np
import json

with open('tetraedr.json', 'r',encoding="utf-8") as json_file:
        tr = json.load(json_file)
        
m=pd.Series(tr) 

ba = []
for i in range(3):
    ba.append(m[1][i] - m[0][i])
    
ca = []
for i in range(3):
    ca.append(m[2][i] - m[0][i])
    
da = []
for i in range(3):
    da.append(m[3][i] - m[0][i])

matrix = np.array([ba,ca,da])
det = np.linalg.det(matrix)
ans = {
    "V":float(det  * 1/6)
}

with open('volume.json','w') as outfile:
        json.dump(ans, outfile)

print(m)