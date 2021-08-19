x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[7,8,9],[4,5,6],[1,2,3]]
r=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]=x[i][j] + y[i][j]
print(r)
