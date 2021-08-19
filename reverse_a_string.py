def reverse(s):
#   str=""
#    for i in s:
#        str=i+str
#    return str
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s=input("Enter a String:")
if(reverse(s)==s):
    print("pallindrome!")
else:
    print("no")
#print(reverse(s))
