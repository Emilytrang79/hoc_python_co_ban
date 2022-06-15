# hoc_python_co_ban
a = int(input('canh tam giac thu nhat: '))
b = int(input('canh tam giac thu hai: '))
c = int(input('canh tam giac thu ba: '))
if ((a+b)>c and (a+c)>b and (b+c)>a):
  print('a,b,c la cac canh cua tam giac')
  if ((a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b)):
    print('tam giac la tam giac vuong')
  elif (a == b and b == c):
    print('tam giac deu')
  elif (a == b or a == c or b == c):
    print('tam giac can')
  elif ((a*a > b*b + c*c) or (b*b > a*a + c*c) or (c*c > b*b + a*a)):
    print('tam giac tu')
  else:
    print('tam giac nhon ')
else:
  print('a,b,c khong la cac canh cua tam giac')
       
        
