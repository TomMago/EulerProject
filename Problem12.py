import numpy as np


def checkdivs(num):
    factors = []
    for x in range(1, int(np.sqrt(num))+1):
        if num % x == 0:
            factors.append(x)
            factors.append(num/x)
    # print(str(num) + ": " + str(factors) + " - " + str(len(factors)))
    return len(factors)


found = False
lastnum = 1
index = 2
while not found:
    if checkdivs(lastnum) > 500:
        print(lastnum)
        found = True
    lastnum += index
    index += 1

# 76576500 in ca. 4 Sekunden
