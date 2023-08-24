alphabet_plus = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ v∨V∧~^→↔()"
alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"

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




def qtd_variables(equation: str, alphabet) -> int:
    '''
    Função usada para contar quantas variáveis (letras) há na equação\nEntrada: String\nSaída: Int
    '''
    variables = []

    alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"

    for logic in (equation):
        for letter in (alphabet):
            if (logic == letter):
                variables.append(logic)
    
    vetor_sem_duplicatas = list(set(variables))  # remove duplicatas
    vetor_sem_duplicatas.sort() # ordena as variáveis
    
    return len(vetor_sem_duplicatas)




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


def lexical_analysis (equation, alphabet_plus):
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



equation = input("Digite uma equação lógica: ")

print(equation)

equation = remove_space(equation)
print(equation)


equacao_valida = bool(lexical_analysis(equation,alphabet_plus) and is_well_formed_formula(equation))
print("Analisador equação:", equacao_valida)

num_variables = qtd_variables(equation, alphabet)
combinations = generate_combinations(num_variables)

print_matrix(combinations, 1)


print(combinations)

##################################################################################################
#  ENTENDER COMO TRANSFORMAR EM FUNÇÃO DEPOIS

def op_parentese (equation):

    pos_final = 0
    i = 0
    equation_vetor = list(equation)

    for var in (equation_vetor):
        if (var == ')' ):
            pos_final = i
        i = i + 1

    if (pos_final == 0):
        
        return equation_vetor

    else:
        vet_invertido = equation[::-1]
        pos_inicial = 0
        i = 0
        for var in (vet_invertido):
            if(var == '(' ):
                pos_inicial = (len(equation)-1) - i
            i = i + 1

        j = pos_inicial
        vetor_especifico = equation[pos_inicial:pos_final+1]

        return vetor_especifico





def pilhas (vetor_especifico):

    pilha_simb = []
    pilha_var = []

    for logic in (vetor_especifico):
        for letter in (alphabet):
            if (logic == letter):
                pilha_var.append(logic)
            else:
                pilha_simb.append(logic)

    
    # pilha_var , pilha_simb
    #while (len(pilha_var) > 0 and len(pilha_simb) > 0):


def op_pilhas (pilha_var, pilha_simb):
    var_i = pilha_var.pop()
    simb = pilha_simb.pop()
    var_f = pilha_var.pop()







'''
 ATÉ O MOMENTO EU CONSEGUI SEPARAR A EXPRESSÃO DO PARENTESE DA PRINCIPAL, AGORA PRECISO RESOLVER A EQUAÇÃO
 MONTANDO 2 PILHAS. 1 PARA AS VARIÁVEIS E A OUTRA PARA OS SÍMBOLOS
'''


# toda vez que eu entrar em um novo conjunto de parenteses, eu devo usar recursão da função para ela começar novamente

# PILHA: pensar em um vetor estilo pilha de pratos (só consigo colocar e tirar por cima)
# FILA: pensar em fila de banco (só consigo adicionar no fim da fila e retirar no começo da fila)