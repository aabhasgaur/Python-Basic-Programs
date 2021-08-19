import math
def factors(n):
    while n%2==0:
        print(2)
        n=n/2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            print(i)
            n=n/i
    if n>2:
        print(n)

n=15
factors(n)
