import matplotlib.pyplot as plt
import numpy as np

a=[]
def num(n):
    a.append(n)
    while n>1:
        if(n%2!=0):
            n=n*3+1
            a.append(n)
        else:
            n=n//2
            a.append(n)
    print(a)
n=int(input("Enter a number:"))
num(n)

x= np.linspace(0,100,len(a))
y=a
plt.plot(x, y, color='blue', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='red', markersize=12)

# Create the plot
plt.plot(x, y)
# Show the plot
plt.show()
