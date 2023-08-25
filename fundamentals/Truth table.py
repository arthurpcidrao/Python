alphabet_plus = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ v∨V∧~^→↔()"
alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
simbolos = "∨V∧~^→↔()v"


def print_matrix (matrix, scalar):
    '''
    Função usada para imprimir na tela o formato de uma matriz
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (j < len(matrix[i]) - 1):
                print(f"{matrix[i][j]*scalar}", end = '  |  ')
            else:
                print(f"{matrix[i][j]*scalar}")




def realizar_operacao(operacao, valor1, valor2):
    if operacao == '∧' or operacao == '^':
        return conjuncao(valor1 == "True", valor2 == "True")
    
    elif operacao == '∨' or operacao == 'V' or operacao == 'v':
        return disjuncao(valor1 == "True", valor2 == "True")
    
    elif operacao == '→':
        return condicional(valor1 == "True", valor2 == "True")
    
    elif operacao == '↔':
        return bicondicional(valor1 == "True", valor2 == "True")
    
    elif operacao == '~':
        return negacao(valor1 == "True")
    
    else:
        return valor2




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


def gerar_combinacoes(num_variaveis):
    '''
    Função que realiza o início da tabela verdade e retorna a matriz inicial.
    '''
    combinacoes = []
    max_value = 2 ** num_variaveis

    for i in range(max_value):
        combinacao = []
        for j in range(num_variaveis):
            bit = (i // (2 ** j)) % 2
            combinacao.append(bit)
        combinacoes.append(combinacao)
    
    return combinacoes



def analise_tab_verdade (equacao, variaveis, num_variaveis):

    combinacoes = gerar_combinacoes(num_variaveis)

    tabela_verdade = []

    for combinacao in combinacoes:
        resultado = avaliar(equacao, variaveis, combinacao)
        tabela_verdade.append(combinacao + [resultado])  # concatenar esse vetor

    return tabela_verdade


def remove_space (equacao):
    count = 0
    for letter in (equacao):
        if (letter == ' '):
            count = count + 1
    
    equacao = equacao.replace(' ', '',count)
    return equacao


def avaliar(equacao, variaveis: list, combinacao):
    pilha_simb = []
    pilha_var = variaveis

    for logic in (equacao):
        for simb in (simbolos):
            if (logic == simb):
                pilha_simb.append(logic)

    for token in equacao:
        if (token in variaveis):
            pilha.append(combinacao[variaveis.index(token)])  # verificar o que faz nessa linha

        elif (token == '('):
            pilha.append(token)
        
        elif (token == ')'):
            while (pilha[-1] != '('):  # pilha[-1] significa o último termo do vetor pilha[]
                pilha.append(realizar_operacao(pilha_simb.pop(), pilha_var.pop(), pilha_var.pop()))
            
            pilha.pop()  # remove o '('
        
        else:
            pilha.append(token)
        
    while (len(pilha) > 1):
        pilha.append(realizar_operacao(pilha.pop(), pilha.pop(), pilha.pop()))

    return pilha[0] == "True"


def analise_parentese(equacao):

    pos_final = 0
    i = 0
    vetor_equacao = list(equacao)

    for var in (vetor_equacao):
        if (var == ')' ):
            pos_final = i
        i = i + 1

    if (pos_final == 0):
        
        return vetor_equacao

    else:
        vet_invertido = equacao[::-1]
        pos_inicial = 0
        i = 0
        for var in (vet_invertido):
            if(var == '(' ):
                pos_inicial = (len(equacao)-1) - i
            i = i + 1

        j = pos_inicial
        vetor_especifico = equacao[pos_inicial:pos_final+1]

        return vetor_especifico




'''
def avaliar(equacao, variaveis, combinacao):
    pilha = []

    tokens = equacao

    for token in tokens:
        if (token in variaveis):
            pilha.append(combinacao[variaveis.index(token)])  # verificar o que faz nessa linha

        elif (token == '('):
            pilha.append(token)
        
        elif (token == ')'):
            while (pilha[-1] != '('):  # pilha[-1] significa o último termo do vetor pilha[]
                pilha.append(realizar_operacao(pilha.pop(), pilha.pop(), pilha.pop()))
            
            pilha.pop()  # remove o '('
        
        else:
            pilha.append(token)
        
    while (len(pilha) > 1):
        pilha.append(realizar_operacao(pilha.pop(), pilha.pop(), pilha.pop()))

    return pilha[0] == "True"
'''

def qtd_variaveis(equacao: str, alphabet) -> int:
    '''
    Função usada para contar quantas variáveis (letras) há na equação\nEntrada: String\nSaída: Int
    '''
    variables = []

    alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"

    for logic in (equacao):
        for letter in (alphabet):
            if (logic == letter):
                variables.append(logic)
    
    vetor_sem_duplicatas = list(set(variables))  # remove duplicatas
    vetor_sem_duplicatas.sort() # ordena as variáveis
    
    return len(vetor_sem_duplicatas)


def quais_variaveis(equacao: str, alphabet) -> int:
    '''
    Função usada para saber quais variáveis (letras) há na equação\nEntrada: String\nSaída: Int
    '''
    variables = []

    alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"

    for logic in (equacao):
        for letter in (alphabet):
            if (logic == letter):
                variables.append(logic)
    
    vetor_sem_duplicatas = list(set(variables))  # remove duplicatas
    vetor_sem_duplicatas.sort() # ordena as variáveis
    
    return vetor_sem_duplicatas


equacao = input("Digite uma equação lógica: ")
print(equacao)

equacao = remove_space(equacao)

num_variaveis = qtd_variaveis(equacao, alphabet)
variaveis = quais_variaveis(equacao, alphabet)

tabela_verdade = analise_tab_verdade(equacao, variaveis, num_variaveis)



