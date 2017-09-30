import numpy as np
sum1 = 0
sum2 = 0
for x in range(1,101):
    sum1 += x
    sum2 += x**2
sum1 = sum1**2
print(sum1-sum2)
