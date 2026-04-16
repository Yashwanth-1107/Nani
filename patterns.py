
row,column = 4,3

mat=[ [1,2,3]
      [4,5,6]
      [7,8,9]
      [4,2,7]
]
res=0
for i in range (row):
    for j in range (column):
        if i==0 or i==row-1 or j==0 or j==column-1:
            res+= mat[i][j]

print(res)            