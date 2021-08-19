num = int(input("Enter a number: "))
temp=num
reverse=0
while num > 0:
    remainder=num%10
    reverse = reverse*10 + remainder
    num = num//10
print("The reverse of the given number is ",reverse)
