# hoc_python_co_ban
a = int(input('so dau: '))
b = int(input('so cuoi: '))
for i in range(a,b+1):
  if (i%3 ==0 and i%5 == 0):
    print('FizzBuzz ' + str(i))
  elif (i%5 == 0):
    print('Buzz ' + str(i))
  elif (i%3 == 0):
    print('Fizz ' + str(i))
  else:
    print(i)

