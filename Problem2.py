sum = 0
fib1 = 1
fib2 = 2
while fib1 <= 4000000:
    if fib1%2==0:
        sum+=fib1
    sw = fib1
    fib1 = fib2
    fib2 = sw + fib1
print(sum)
