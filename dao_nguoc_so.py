# hoc_python_co_ban
a = int(input(''))
reverse_a = 0
while (a // 10 > 0):
  reverse_a = reverse_a * 10 + a % 10
  a = a // 10
print(reverse_a * 10 + a)
