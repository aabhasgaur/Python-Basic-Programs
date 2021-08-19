import random
import string
print("Hello, Welcome to the Random Password Generator!")
length=int(input("Enter the length of the Password:"))

#Define Data
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

#combine the data
all=lower + upper + num + symbols

#use random
temp= random.sample(all,length)

#creating Password
print("".join(temp))
