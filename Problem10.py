import numpy as np

SIZE = 2000000
STOP = np.sqrt(SIZE)

x = np.arange(2,SIZE)

#print("Debug: {}".format(x))

for num in x:
    if num > STOP:
        break
    x = x[(x%num!=0) | (num == x)]
    print("Debug2: {}".format(x) + "; num: {}".format(num))

print(np.sum(x))

#142913828922 in 3.36 sekunden
