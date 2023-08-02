from random import random

def read_matrix (linhas, colunas):

    matrix = [None]*linhas

    for i in range(len(matrix)):
        matrix[i] = [None]*colunas
    
    return matrix

def input_zeros (matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    
    return matrix



def input_values (matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(random()*101)
            if (float(matrix[i][j]) > 100):
                matrix[i][j] = float(random()*100)
    
    return matrix



def print_matrix (matrix, scalar):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (j < len(matrix[i]) - 1):
                print(f"{matrix[i][j]*scalar:.2f}", end = '    ')
            else:
                print(f"{matrix[i][j]*scalar:.2f}")



def read_matrix_T (linhas, colunas, matrix):

    matrix_T = read_matrix(colunas, linhas)

    for i in range(len(matrix_T)):
        for j in range(len(matrix_T[i])):
            matrix_T[i][j] = matrix[j][i]
    
    return matrix_T



def sum_matrix (matrix_1, matrix_2):    
    
    matrix_s = read_matrix(len(matrix_1), len(matrix_1[0]))
    
    for i in range(len(matrix_s)):
        for j in range(len(matrix_s[i])):
            matrix_s[i][j] = matrix_1[i][j] + matrix_2[i][j]
    
    return matrix_s



def print_diagonal_principal (matrix, scalar):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (i == j):
                print(f"{matrix[i][j]*scalar:.2f}", end = "    ")
            else:
                print("        ", end = " ")
            
        print()



def print_secundaria_principal (matrix, scalar):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (i+j == len(matrix)-1):
                print(f"{matrix[i][j]*scalar:.2f}", end = "    ")
            else:
                print("        ", end = " ")
            
        print()



def maior_elemento (matrix):

    maior = matrix[0][0]
    linha = 0
    coluna = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if (matrix[i][j] > maior):
                maior = matrix[i][j]
                linha = i
                coluna = j
    
    return maior, linha, coluna



def print_diagonal_acima (matrix, scalar):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (j >= i):
                print(f"{matrix[i][j]*scalar:.2f}", end = "    ")
            else:
                print("        ", end = " ")
            
        print()



def print_diagonal_abaixo (matrix, scalar):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (j <= i):
                print(f"{matrix[i][j]*scalar:.2f}", end = "    ")
            else:
                print("        ", end = " ")
            
        print()



def menor_elemento (matrix):

    menor = matrix[0][0]
    linha = 0
    coluna = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if (matrix[i][j] < menor):
                menor = matrix[i][j]
                linha = i
                coluna = j
    
    return menor, linha, coluna



def sum_vector (matrix):
    if (len(matrix) == 1):
        sum = 0
        for j in range(len(matrix[0])):
            sum = matrix[0][j] + sum
        
        average = sum/len(matrix[0])
        
        return average
    
    elif (len(matrix[0]) == 1):
        sum = 0
        for i in range(len(matrix)):
            sum = matrix[i][0] + sum
        
        average = sum/len(matrix)
        
        return average

    elif ((len(matrix) == 1) and (len(matrix[0]) == 1)):
        sum = matrix[0][0]
    
        return sum
    
    else:
        m_linhas = read_matrix(1, len(matrix[0]))
        m_colunas = read_matrix(len(matrix), 1)

        for j in range(len(matrix[0])):
            sum_linhas = 0
            for i in range(len(matrix)):
                sum_linhas = matrix[i][j] + sum_linhas
            
            m_linhas[0][j] = sum_linhas/(len(matrix))
        
        for i in range(len(matrix)):
            sum_colunas = 0
            for j in range(len(matrix[0])):
                sum_colunas = matrix[i][j] + sum_colunas
            
            m_colunas[i][0] = sum_colunas/len(matrix[0])

        return m_linhas, m_colunas
    


def prime_number (matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            div = 0
            for k in range(1,(int(matrix[i][j])+1)):
                if ( int(matrix[i][j]) % k == 0):
                    div = div + 1
            
            if(div == 2):
                count = count + 1
    
    return print(f"considerando a parte inteira da matriz, existem {count} números primos!")



def input_z (matrix, vetor):
    if (len(matrix[0]) > 1):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i == j):
                    matrix[i][j] = vetor[0][j]
                else:
                    matrix[i][j] = 0
    
    elif (len(matrix) > 1):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i == j):
                    matrix[i][j] = vetor[i][0]
                else:
                    matrix[i][j] = 0    
    
    return matrix



def input_z_reverse (matrix, vetor):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j):
                vetor[i][0] = matrix[i][j]
    
    return vetor



def sum_terms (matrix):

    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum = matrix[i][j] + sum

    return sum



def product_matrix (matrix, matrix_a, matrix_b):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            sum = 0

            for k in range(len(matrix_a[0])):
                sum = matrix_a[i][k]*matrix_b[k][j] + sum
            
            matrix[i][j] = sum
    
    return matrix



def traco_matrix (matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == j):
                sum = matrix[i][j] + sum
    
    return sum



def prod_pp (matrix_1, matrix_2):

    matrix_pp = read_matrix(len(matrix_1), len(matrix_1[0]))

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            matrix_pp[i][j] = matrix_1[i][j]*matrix_2[i][j]
    
    return matrix_pp



def ordem_matrix_C (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):

                    if (matrix[i][j] > matrix[k][l]):
                        aux = matrix[k][l]
                        matrix[k][l] = matrix[i][j]
                        matrix[i][j] = aux
    return matrix



def ordem_matrix_D (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):

                    if (matrix[i][j] < matrix[k][l]):
                        aux = matrix[k][l]
                        matrix[k][l] = matrix[i][j]
                        matrix[i][j] = aux
    return matrix



def laplace(matrix_n, coluna):

    mat = [None]*(len(matrix_n) - 1)

    for i in range(len(mat)):
        mat[i] = [None]*len(mat)
    
    for i in range(len(mat)):
        k = 0
        for j in range(len(mat[i])):
            if (k == coluna):
                k = k + 1
            mat[i][j] = matrix_n[i+1][k]
            k = k + 1
    
    #print_matrix(mat, 1)
    #print()

    if (len(matrix_n) == 1):
        return 1

    elif (len(mat) == 2):
        return float(mat[0][0])*float(mat[1][1]) - float(mat[0][1])*float(mat[1][0])

    else:
        det_parc = 0
        for j in range(len(mat[0])):
            det_parc = ((-1)**j)*float(mat[0][j])*laplace(mat, j) + det_parc
        
        return det_parc