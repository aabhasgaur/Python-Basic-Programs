n=3
def areSame(A,B):

   for i in range(n):
      for j in range(n):
         if (A[i][j] != B[i][j]):
            return 0
   return 1
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]

if (areSame(x,y)==1):
   print("Matrices are identical.")
else:
   print("Matrices are not identical.")
