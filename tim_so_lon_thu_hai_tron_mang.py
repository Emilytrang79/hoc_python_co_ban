num = [2,5,11,15,8]
max_1 = num[0]
for i in range(0, len(num)):
  if (num[i] > max_1):
    max_1 = num[i]
max_2 = num[0]
for j in range(0, len(num)):
  if (num[j] > max_2 and num[j] != max_1):
    max_2 = num[j]
print(max_2)
  
