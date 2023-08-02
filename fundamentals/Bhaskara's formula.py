#a*x^2 + b*x + c = 0
print("Digite os números (a b c) na mesma linha com um espaço de separação: ")
a,b,c = input().split(' ')

a=float(a)
b=float(b)
c=float(c)

delta = b**2 - 4*a*c

if a == 0:
  print('Impossivel calcular')

else:

  if delta < 0:
    print('Impossivel calcular')

  else :
    x1= (-b + delta**(0.5))/(2*a)
    x2= (-b - delta**(0.5))/(2*a)

    print('R1 = {:.5f}\nR2 = {:.5f}'.format(x1,x2))
