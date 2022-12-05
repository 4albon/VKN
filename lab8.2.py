import numpy as np

q = np.random.randint(0,30,(3,3))
print(q)
r = q * 2
r = r + q
print(r)

res = r[0][0] * r[0][2] * r[2][0] * r[2][2]
print(res)