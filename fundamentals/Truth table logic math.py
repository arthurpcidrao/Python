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




def qtd_variables(equation: str) -> int:
    '''
    Função usada para contar quantas variáveis (letras) há na equação\nEntrada: String\nSaída: Int
    '''
    variables = 0

    alphabet = "abcdefghijklmnopqrstuwxyz"

    for logic in (equation):
        for letter in (alphabet):
            if (logic == letter):
                variables = variables + 1
    
    return variables




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


'''
def results_truth_table(combinations):
    
    resp = [None]*len(combinations)
    vector = [None]*len(combinations[0])

    for i in range(len(combinations[0])):
        vector[i] = [None]*len(combinations)
    
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            vector[i][j] = combinations[j][i]
    
    for i in range(len(resp)):

        resp[i] = bool(vector[i][0] and vector[i][1])

    return resp

'''
alphabet = "abcdefghijklmnopqrstuvwxyzç ∨V∧~^→↔()"

def lexical_analysis (equation, alphabet):
    sum = 0

    for logic in (equation):
        for letter in (alphabet):
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
    
    equation_m = equation.replace(' ', '',count)
    print(equation_m)

    is_well_formed_formula(equation_m)



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



#sentense = input("Digite uma frase: ")
equation = input("Digite uma equação lógica: ")

#sentense_analysis(sentense)
#lexical_analysis(equation, alphabet)

print(equation)
#result_syntax = is_well_formed_formula(equation)
#print("Analisador Sintático:", result_syntax)

equacao_valida = bool(lexical_analysis(equation,alphabet) and is_well_formed_formula(equation))
print("Analisador equação:", equacao_valida)

num_variables = qtd_variables(equation)
combinations = generate_combinations(num_variables)

print_matrix(combinations, 1)
'''resp = results_truth_table(combinations)

for i in range(len(resp)):
    print(resp)
'''

print(combinations)

# toda vez que eu entrar em um novo conjunto de parenteses, eu devo usar recursão da função para ela começar novamente
