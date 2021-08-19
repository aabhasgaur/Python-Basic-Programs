num = int(input("Enter a number: "))
temp=num
reverse=0
while num > 0:
    remainder=num%10
    reverse = reverse*10 + remainder
    num = num//10
if reverse == temp:
    print("The given number is a PALLINDROME! ")
else:
    print("The given number is not a pallindrome. ")
