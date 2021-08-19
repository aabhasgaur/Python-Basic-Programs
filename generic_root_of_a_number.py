#Generic root is the sum of the digits of a number until we get a single digit number
#generic root of 245 is 2+4+5=11 then 11 is done the same way,ie, 1+1=2
#therefore generic root of 245 is 2.

num=int(input("Enter a number:"))
def Generic(self):
    while num>10:
        sum=0
        while num:
            r=num%10
            num=num/10
            sum+=r
        if sum >=10:
            num=sum
        else:
            break
print("Generic root of the number is",int(sum))
