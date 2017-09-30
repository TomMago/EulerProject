found = 0
num = 2
while found <= 10000:
    prime = True
    for x in range(2,num):
        if num%x==0:
            prime = False
            break
    if prime:
        found+=1
        print("{}. Primzahl".format(found) + ": {}".format(num))
    num+=1

##10001. Primzahl: 104743 gefunden in 49s
