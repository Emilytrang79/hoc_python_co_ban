num = [2,5,9,3,7]
max_1 = num[0]
for i in range(0, len(num)):
  if (num[i] > max_1):
    max_1 = num[i]
for j in range(0, len(num)):
  max_2 = num[0]
  if (num[j] > max_2 and max_2 != max_1):
    max_2 = num[j]
print(max_2)
  
    
