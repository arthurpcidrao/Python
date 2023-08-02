# Digite valores e saiba quantos são positivos (even numbers)

a=int(input("Digite um número: "))
b=int(input("Digite um número: "))
c=int(input("Digite um número: "))
d=int(input("Digite um número: "))
e=int(input("Digite um número: "))

x=[a,b,c,d,e]

count=0
count=int(count)

for i in range(0,5):
  if x[i]%2 == 0:
    count=count+1

print('{} valores pares'.format(count))