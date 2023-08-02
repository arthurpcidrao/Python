# Digite um valor numérico e saiba como esse valor será dado em cédulas (reais)

valor = int(input("Digite um valor: R$ "))
print(valor)

n100 = int(valor/100)
valor = valor - n100*100

n50 = int(valor/50)
valor = valor - n50*50

n20 = int(valor/20)
valor = valor - n20*20

n10 = int(valor/10)
valor = valor - n10*10

n5 = int(valor/5)
valor = valor - n5*5

n2 = int(valor/2)
valor = valor - n2*2

n1 = valor

print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(valor))