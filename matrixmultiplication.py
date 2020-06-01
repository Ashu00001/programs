x=[[1,2,3],
    [3,5,6],
    [1,7,2]]
y=[[6,5,7],
     [7,8,9], 
     [3,4,5]]
z=[[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(len(x)):
    for j in range (len(y)):
        for k in range(len(y)):
            z[i][j]+=x[i][k]*y[k][j]
for r in z:
    print(r)  
