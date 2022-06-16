num = [ [9,1,15,26,5],
       [8,22,98,7,84],
       [6,2,3,10,12] ]
max = num[0][0]
for i in range(0,len(num)):
  for j in range(0,len(num[i])):
    if num[i][j] > max:
      max = num[i][j]
print(max)
