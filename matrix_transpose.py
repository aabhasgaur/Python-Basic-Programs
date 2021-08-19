x=[[1,2],[4,5],[7,8]]
r=[[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i]=x[i][j]
print(r)
