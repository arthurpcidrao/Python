# digite vários números e o programa retornará o menor deles

print("Digite os números na mesma linha com um espaço entre eles: ")
array = input().split(' ')

menor = int(array[0])
indice = 0
i = int(0)
for i in range(0,len(array)):
    if (menor > int(array[i])):
        menor = int(array[i])
        indice = i
    i = i+1

print(f"Menor valor: {menor}")
print(f"Posição: {indice}")
