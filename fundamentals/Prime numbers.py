# Digite números e saiba se é primo ou não

n = int(input("Digite quantos números você quer testar: "))

lista = []

i = int(0)

for i in range(0,n):
    print(f"Digite o {i+1}º número teste: ")
    lista.append(int(input()))
    
    j = int(1)
    div = 0
    for j in range(1,int(lista[i])+1):
        if (int(lista[i])%j == 0):
            div = div+1
        j = j+1

    
    if (div == 2):
        print(f"{lista[i]} é primo")
    else:
        print(f"{lista[i]} nao é primo")
    
    i=i+1
