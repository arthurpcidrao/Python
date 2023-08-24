alphabet_plus = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ v∨V∧~^→↔()"
alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
simbolos = "∨V∧~^→↔()v"

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


def analise_tab_verdade (equacao, num_variaveis):

    combinacoes = gerar_combinacoes(num_variaveis)

    tabela_verdade = []

    for i in combinacoes:
        resultado = avaliar(equacao, variaveis, combinacao)
        tabela_verdade.append(i + [resultado])  # concatenar esse vetor

    return tabela_verdade


def remove_space (equacao):
    count = 0
    for letter in (equacao):
        if (letter == ' '):
            count = count + 1
    
    equacao = equacao.replace(' ', '',count)
    return equacao



def avaliar(equacao, num_variaveis, valores):
    pilha = []

    tokens = remove_space(equacao)
    

