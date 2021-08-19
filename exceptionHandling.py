try:
    length=100
    breadth=0
    print(area=length/breadth)
except Exception:
    print("Division by zero is invalid! Kindly change your input.")

del(breadth)

try:
    breadth=0
    print(area=length/breadth)
except NameError:
    print("Variable not assigned.")
except ZeroDivisionError:
    print("Division by zero is invalid! Kindly change your input.HAHAHA")
