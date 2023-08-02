# Digite valores e saiba quantos são maiores que zero

a=float(input("Digite um numero: "))
b=float(input("Digite um numero: "))
c=float(input("Digite um numero: "))
d=float(input("Digite um numero: "))
e=float(input("Digite um numero: "))
f=float(input("Digite um numero: "))

x=[a,b,c,d,e,f]
count=0
count=int(count)

for i in range (0,6):
  if (x[i]>0):
    count=count+1

print('{} valores positivos'.format(count))
