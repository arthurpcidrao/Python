import ttg

alphabet_plus = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ vV∧~^→↔()"
alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
simbolos = "V∧~^→↔v"
simbolos_plus = "V∧~^→↔v()"



def realizar_operacao(operacao, valor1, valor2):
    if (operacao == '∧') or (operacao == '^'):
        return conjuncao(valor1, valor2)
    
    elif (operacao == 'V') or (operacao == 'v'):
        return disjuncao(valor1, valor2)
    
    elif operacao == '→':
        return condicional(valor1, valor2)
    
    elif operacao == '↔':
        return bicondicional(valor1, valor2)
    
    elif operacao == '~':
        return negacao(valor1)



def conjuncao(valor1, valor2):
    return valor1 and valor2

def disjuncao(valor1, valor2):
    return valor1 or valor2

def condicional(valor1, valor2):
    return not valor1 or valor2

def bicondicional(valor1, valor2):
    return (not valor1 or valor2) and (not valor2 or valor1)

def negacao(valor):
    return not valor



def print_matrix (matrix, scalar):
    '''
    Função usada para imprimir na tela o formato de uma matriz
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (j < len(matrix[i]) - 1):
                print(f"{matrix[i][j]*scalar}", end = '   |   ')
            else:
                print(f"{matrix[i][j]*scalar}")



def qtd_variables(equation):
    '''
    Função usada para contar quantas variáveis (letras) há na equação\nEntrada: String\nSaída: Int
    '''
    variables = []

    for logic in (equation):
        for letter in (alphabet):
            if (logic == letter):
                variables.append(logic)
    
    vetor_sem_duplicatas = list(set(variables))  # remove duplicatas
    vetor_sem_duplicatas.sort() # ordena as variáveis
    
    return vetor_sem_duplicatas



def read_matrix_T (linhas, colunas, matrix):#usar para combinations

    matrix_T = read_matrix(colunas, linhas)

    for i in range(len(matrix_T)):
        for j in range(len(matrix_T[i])):
            matrix_T[i][j] = matrix[j][i]
    
    return matrix_T



def read_matrix (linhas, colunas):

    matrix = [None]*linhas

    for i in range(len(matrix)):
        matrix[i] = [None]*colunas
    
    return matrix



def generate_combinations(num_variables):
    '''
    Função que realiza o início da tabela verdade e retorna a matriz inicial.
    '''
    combinations = []
    max_value = 2 ** num_variables

    for i in range(max_value):
        combination = []
        for j in range(num_variables):
            bit = (i // (2 ** j)) % 2
            combination.append(bit)
        combinations.append(combination)
    
    return combinations



def qtd_operacoes (equation):
    operacoes = 0
    
    for i in equation:
        for j in simbolos:
            if (i == j):
                operacoes = operacoes + 1
    
    return operacoes



def lexical_analysis (equation):
    sum = 0

    for logic in (equation):
        for letter in (alphabet_plus):
            if (logic == letter):
                sum = sum + 1

    if (sum == len(equation)):
        return True
    
    else:
        return False
    


def remove_space (equation):
    count = 0
    for letter in (equation):
        if (letter == ' '):
            count = count + 1
    
    equation = equation.replace(' ', '',count)
    return equation



def is_well_formed_formula(input_formula):
    # Função para remover os espaços em branco da fórmula
    def remove_spaces(formula):
        return formula.replace(" ", "")
    
    input_formula = remove_spaces(input_formula)
    stack = []  # Usaremos uma pilha para verificar a correspondência de parênteses
    
    # Itera sobre cada caractere na fórmula de entrada
    i = 0  # Variável para manter o índice atual
    while i < len(input_formula):
        char = input_formula[i]
        
        if char == '(':  # Se encontrar um parêntese de abertura
            # Verifica se o próximo caractere é um parêntese de fechamento
            next_char = input_formula[i + 1] if i + 1 < len(input_formula) else ''
            if next_char == ')':
                return False  # Parêntese vazio encontrado
            stack.append('(')  # Adiciona à pilha
        elif char == ')':  # Se encontrar um parêntese de fechamento
            if len(stack) == 0 or stack[-1] != '(':  # Verifica se a pilha está vazia ou não corresponde ao esperado
                return False  # Se não corresponder, a análise sintática falha
            stack.pop()  # Se corresponder, remove o último parêntese de abertura da pilha
        
        i += 1  # Incrementa o índice
    
    return len(stack) == 0  # A análise sintática é bem-sucedida se a pilha estiver vazia



def analise(combination_n, combination_t, equation, variables):
    pilha_var = []
    pilha_simb = []

    for var in equation:
        if var in alphabet:
            pilha_var.append(var)
        elif var in simbolos:
            while pilha_simb and pilha_simb[-1] != '(' and simbolos.index(pilha_simb[-1]) >= simbolos.index(var):
                pilha_var.append(pilha_simb.pop())
            pilha_simb.append(var)

    while pilha_simb:
        pilha_var.append(pilha_simb.pop())

    vetor = []
    for j in range(len(combination_n)):
        resultados_var = []
        for var in pilha_var:
            if var in variables:
                resultados_var.append(combination_t[variables.index(var)][j])
            else:
                if var == '~':
                    resultado = realizar_operacao(var, resultados_var.pop(), 0)
                else:
                    resultado = realizar_operacao(var, resultados_var.pop(), resultados_var.pop())
                resultados_var.append(resultado)
        vetor.append(resultados_var[0])  # O resultado final da expressão está no topo da pilha
    
    for i in range (len(vetor)):
        if (vetor[i] == True):
            vetor[i] = 1
        elif (vetor[i] == False):
            vetor[i] = 0

    return vetor



equation = input("Digite uma equação lógica: ")
equation = remove_space(equation)
print(equation)

count = 0;
for i in equation:
    if (i == '~'):
        #equation = equation.replace('~', '',count)
        equation.insert(count - 1,' ')
        equation.insert(count + 2, ' ')
    
    if ((i == 'v')):
        equation = equation.replace('v', "or", count)
        equation.insert(count - 1,' ')
        equation.insert(count + 2, ' ')

    if ((i == 'V')):
        equation = equation.replace('V', "or", count)
        equation.insert(count - 1,' ')
        equation.insert(count + 2, ' ')

equacao_valida = bool(lexical_analysis(equation) and is_well_formed_formula(equation))
print(f"A equação é válida: {equacao_valida}")

variables = qtd_variables(equation)
num_variables = len(variables)

print(variables)

print(ttg.Truths(variables))

'''
combinations_n = generate_combinations(num_variables)
combination_t = read_matrix_T(len(combinations_n), len(combinations_n[0]), combinations_n)
qtd = qtd_operacoes(equation)

print(qtd)
print(combination_t)
respostas = analise(combinations_n, combination_t, equation, variables)
print(respostas)

combination_t.append(respostas)  # incluindo as respostas
print(combination_t)
combination = read_matrix_T(len(combination_t), len(combination_t[0]), combination_t)

variables.append(equation)

print()
for i in range(len(variables)):
    print(variables[i], end = '       ')

print()
for i in range(len(variables)*7):
    print('-', end = '')

print()
print_matrix(combination, 1)
print()
'''
