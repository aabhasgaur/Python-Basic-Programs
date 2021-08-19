def areSame(A,B):

   for i in range(n):
      for j in range(n):
         if (A[i][j] != B[i][j]):
            return 0
   return 1
A=[]
n=int(input("Enter n for n x n matrix : "))
print("Enter the element ::>")
for i in range(n):
   row = []
   for j in range(n):
      row.append(int(input()))
   A.append(row)

print(A)
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(A[i][j], end=" ")
   print()

B=[]
n=int(input("Enter N for N x N matrix : "))
print("Enter the element ::>")
for i in range(n):
   row = []
   for j in range(n):
      row.append(int(input()))
   B.append(row)

print(B)
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(B[i][j], end=" ")
   print()

if (areSame(A, B)==1):
   print("Matrices are identical")
else:
   print("Matrices are not identical")
