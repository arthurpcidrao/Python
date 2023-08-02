# Média de alunos

i = 0
x = 1
soma = 0

while (x != 2):

    if(i < 2):
        nota = float(input())
        if ((nota>=0) and (nota<=10)):
            i = i+1
            soma = soma + nota
        else:
            print("nota invalida")

    else: 
        if (x == 1):  
            media = soma/i
            print(f"media = {media:.2f}")
            
        x = int(input("novo calculo (1-sim 2-nao)\n"))
        if (x == 1):
            i = 0
            soma = 0