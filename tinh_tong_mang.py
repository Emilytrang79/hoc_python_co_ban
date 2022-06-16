num = [
  [1,4,5,6, 7, 8],
  [4,6,2,7, 7, 8],
  [7,9,4,2, 7, 8]
]
for a in range(0,len(num[0])):
  sum = 0
  for j in range(0, len(num)):
    sum += num[j][a]
  print(sum)

    
