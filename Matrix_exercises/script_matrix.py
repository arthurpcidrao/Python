from funções_trabalho_AV3 import *

question = 0
pros = 1
while((question < 12) and (pros == 1)):
    print("############################################################")
    linhas_a = int(input("digite o número de linhas da matriz/vetor A: "))
    colunas_a = int(input("digite o número de colunas da matriz/vetor A: "))
    linhas_b = int(input("\ndigite o número de linhas da matriz/vetor B: "))
    colunas_b = int(input("digite o número de colunas da matriz/vetor B: "))

    matrix_a = input_values(read_matrix(linhas_a, colunas_a))
    matrix_b = input_values(read_matrix(linhas_b, colunas_b))

    print("-------------------------------------------------------")
    print("Matriz A:\n")
    print_matrix(matrix_a, 1)

    print()
    print("Matriz B:\n")
    print_matrix(matrix_b, 1)
    print("-------------------------------------------------------")

    question = int(input("Digite a questão que você deseja exibir: "))
    print()

    if(question == 1):
        print("Questão 1)\n")

        x = int(input("Digite um número inteiro x: "))
        y = int(input("Digite um número inteiro y: "))

        print("\nMatriz A*x = \n")
        print_matrix(matrix_a, x)
        print("\nMatriz B*y = \n")
        print_matrix(matrix_b, y)
        print()
    
    elif(question == 2):
        print("Questão 2)\n")

        matrix_c = read_matrix_T(linhas_a, colunas_a, matrix_a)
        matrix_d = read_matrix_T(linhas_b, colunas_b, matrix_b)

        print("\nMatriz C(At) = \n")
        print_matrix(matrix_c, 1)
        print("\nMatriz D(Bt) = \n")
        print_matrix(matrix_d, 1)
        print()
    
    elif(question == 3):
        print("Questão 3)\n")

        if ((linhas_a == linhas_b) and (colunas_a == colunas_b)):
            matrix_s = sum_matrix(matrix_a, matrix_b)
            
            print("Matriz A + B = \n")
            print_matrix(matrix_s, 1)
            print()

        else:
            print("As linhas e colunas de A devem ser iguais as linhas e colunas de B\n")

    elif(question == 4):
        print("Questão 4)\n")

        if (linhas_a == colunas_a):
            print("Diagonal principal:\n")
            print_diagonal_principal (matrix_a, 1)

            print("\n Diagonal secundária:\n")
            print_secundaria_principal (matrix_a, 1)

        else:
            maior, linha, coluna = maior_elemento(matrix_a)
            print(f"maior elemento: {maior:.2f}")
            print(f"linha: {linha}")
            print(f"coluna: {coluna}")
    
    elif(question == 5):
        print("Questão 5)\n")

        if (linhas_b == colunas_b):
            print("Elementos da diagonal principal e acima:\n")
            print_diagonal_acima(matrix_b, 1)

            print("\nElementos da diagonal principal e abaixo:\n")
            print_diagonal_abaixo(matrix_b, 1)
            
        else:
            menor, linha, coluna = menor_elemento(matrix_b)
            print(f"menor elemento: {menor:.2f}")
            print(f"linha: {linha}")
            print(f"coluna: {coluna}")

    elif(question == 6):
        print("Questão 6)\n")
        
        if ((len(matrix_a) > 1) and (len(matrix_a[0]) > 1)):
            m_linhas, m_colunas = sum_vector(matrix_a)
            print("M_linhas:\n")
            print_matrix(m_linhas, 1)
            print("\nM_colunas:\n")
            print_matrix(m_colunas, 1)
            print()
        
        else:
            average = sum_vector(matrix_a)
            print(f"Média: {average:.2f}")
    
    elif(question == 7):
        print("Questão 7)\n")
        
        if ((linhas_b != colunas_b) and ((linhas_b > 1) or (colunas_b > 1))):
            matrix_x = print_matrix(read_matrix_T(linhas_b, colunas_b, matrix_b), 2.5)
        
        else:
            prime_number(matrix_b)

    elif(question == 8):
        print("Questão 8)\n")
        n = int(input("Digite o número 0 ou o número 1: "))

        while((n != 0) and (n != 1)):
            n = int(input("Digite SOMENTE 0 ou 1: "))

        if (n == 1):
            z = sum_matrix(input_zeros(read_matrix(linhas_a, colunas_a)), matrix_a)
        
        elif (n == 0):
            z = sum_matrix(input_zeros(read_matrix(linhas_b, colunas_b)), matrix_b)
        
        if ((len(z) == 1) and (len(z[0]) > 1)):
            print()
            z_linhas = read_matrix(len(z[0]), len(z[0]))
            z_linhas = input_z(z_linhas, z)
            print_matrix(z_linhas, 1)
            print()

        elif (len(z[0]) == 1 and (len(z) > 1)):
            print()
            z_colunas = read_matrix(len(z), len(z))
            z_colunas = input_z(z_colunas, z)
            print_matrix(z_colunas, 1)
            print()
        
        elif (len(z) == len(z[0])):
            print()
            z_vector = read_matrix(len(z), 1)
            z_vector = input_z_reverse(z, z_vector)
            print_matrix(z_vector, 1)
        
        else:
            print()
            sum = sum_terms(z)
            print(f"Soma dos termos = {sum:.2f}")
            print()

    elif(question == 9):
        print("Questão 9)\n")

        if (len(matrix_a[0]) == (len(matrix_b))):
            matrix_prod = read_matrix(len(matrix_a), len(matrix_b[0]))
            matrix_prod = product_matrix(matrix_prod, matrix_a, matrix_b)
            print_matrix(matrix_prod, 1)
            print()
        
        else:
            print("não é possível realizar o produto entre essas matrizes.")
    
    elif(question == 10):
        print("Questão 10)\n")

        if ((len(matrix_a) == len(matrix_a[0])) and (len(matrix_b) == len(matrix_b[0]))):
            matrix_c = read_matrix_T(linhas_a, colunas_a, matrix_a)
            matrix_d = read_matrix_T(linhas_b, colunas_b, matrix_b)
            matrix_prod = read_matrix(len(matrix_b), len(matrix_b))

            termo_1 = traco_matrix(prod_pp(matrix_a, matrix_c))
            termo_2 = traco_matrix(product_matrix(matrix_prod, matrix_d, matrix_b))*2

            print(f"Valor da expressão é = {termo_1+termo_2:.2f}")
            print()
        
        else:
            matrix_a = ordem_matrix_C(matrix_a)
            matrix_b = ordem_matrix_D(matrix_b)

            print("Matriz A ordenada crescente:\n")
            print_matrix(matrix_a, 1)
            print("\nMatriz B ordenada decrescente:\n")
            print_matrix(matrix_b, 1)
    
    elif(question == 11):
        print("Questão 11) - Determinante da Matriz A\n")

        if (linhas_a == colunas_a):

            det = 0
    
            for j in range(len(matrix_a[0])):
                det = ((-1)**j)*float(matrix_a[0][j])*laplace(matrix_a, j) + det
            
            print(f"Determinante = {det:.2f}")

        else:
            print("Não é possível calcular o determinante")
    
    else:
        break

    print("\nDeseja continuar? (1) - sim  |  (qualquer outro número) - não")
    pros = int(input())

print("############################################################")
print("Obrigado!")
