def dec1(num1, num2):
    if checkpal(num1*num2):
        print(num1,num2,num1*num2)
    else:
        dec1(num1-1,num2)


def checkpal(num):
    st = str(num)
    if st==st[::-1]:
        #print(num)
        return True

for x in range(999,100,-1):
    dec1(999,x)
