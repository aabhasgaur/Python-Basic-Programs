def replace(num):
    num += calculate(num)
    return num

def calculate(num):
    result=0
    decimalPlace=1

    if(num==0):
        result+=(7*decimalPlace)
    while(num>0):
        if(num%10==0):
            result+=(7*decimalPlace)
        num=num//10
        decimalPlace=decimalPlace*10
    return result

num=int(input("Enter a number:"))
print(replace(num))
