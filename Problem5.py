num = 21
while True:
    divi = True
    for x in range(1,20):
        if not num%x==0:
            divi = False
            break
    if divi:
        print(num)
        break
    num += 1
    print(num)
