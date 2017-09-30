import numpy as np


def checktrip(a, b, c):
    if(a**2+b**2==c**2):
        return True
    else:
        return False

found = False
for c in range(1,1000):
    for b in range(1, c):
        for a in range(1, b):
            if checktrip(a,b,c) and a+b+c==1000:
                print(a,b,c)
                print("Produkt: {}".format(a*b*c))
                found = True
                break
        if found:
            break
    if found:
        break

#200 375 425
#Produkt: 31875000 in ca 13 sekkunden
