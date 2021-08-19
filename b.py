def findValue(a,b):
    a=a[::-1]
    b=b[::-1]
    if(a.find(b)==0):
        print('Yes')
    else:
        print('No')
x=input()
y=input()
findValue(x,y)
