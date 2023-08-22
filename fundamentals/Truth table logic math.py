'''def sentense_analysis (sentense):

    array = sentense.split(' ')
    i = 0
    for logic in (array):
        
        if (logic == "ou"):
            array[i] = 'v'
        i = i+1

    print(array)
'''

def qtd_variables(equation):
    variables = 0

    alphabet = "abcdefghijklmnopqrstuwxyz"

    for logic in (equation):
        for letter in (alphabet):
            if (logic == letter):
                variables = variables + 1
    
    return variables


def print_matrix (matrix, scalar):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (j < len(matrix[i]) - 1):
                print(f"{matrix[i][j]*scalar}", end = '  |  ')
            else:
                print(f"{matrix[i][j]*scalar}")



def generate_combinations(num_variables):
    combinations = []
    max_value = 2 ** num_variables

    for i in range(max_value):
        combination = []
        for j in range(num_variables):
            bit = (i // (2 ** j)) % 2
            combination.append(bit)
        combinations.append(combination)
    
    return combinations



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




def lexical_analysis (equation):
    alphabet = "abcdefghijklmnopqrstuvwxyzç ∨V∧~^→↔()"
    sum = 0

    for logic in (equation):
        for letter in (alphabet):
            if (logic == letter):
                sum = sum + 1

    if (sum == len(equation)):
        print("Os símbolos estão corretos")

        remove_space(equation)
    
    else:
        print("Os símbolos estão errados")





def remove_space (equation):
    count = 0
    for letter in (equation):
        if (letter == ' '):
            count = count + 1
    
    equation_m = equation.replace(' ', '',count)
    print(equation_m)

    #is_well_formed_formula(equation_m)



'''
def is_well_formed_formula(equation_m):
    
    equation_m = remove_space(equation_m)
    stack = []  # Usaremos uma pilha para verificar a correspondência de parênteses
    
    # Itera sobre cada caractere na fórmula de entrada
    i = 0  # Variável para manter o índice atual
    while i < len(equation_m):
        char = equation_m[i]
        
        if char == '(':  # Se encontrar um parêntese de abertura
            # Verifica se o próximo caractere é um parêntese de fechamento
            next_char = equation_m[i + 1] if i + 1 < len(equation_m) else ''
            if next_char == ')':
                return False  # Parêntese vazio encontrado
            stack.append('(')  # Adiciona à pilha
        elif char == ')':  # Se encontrar um parêntese de fechamento
            if len(stack) == 0 or stack[-1] != '(':  # Verifica se a pilha está vazia ou não corresponde ao esperado
                return False  # Se não corresponder, a análise sintática falha
            stack.pop()  # Se corresponder, remove o último parêntese de abertura da pilha
        
        i += 1  # Incrementa o índice
    
    return len(stack) == 0  # A análise sintática é bem-sucedida se a pilha estiver vazia

# Exemplo de input
'''


#sentense = input("Digite uma frase: ")
equation = input("Digite uma equação lógica: ")

#sentense_analysis(sentense)
lexical_analysis(equation)

print(equation)


num_variables = qtd_variables(equation)
combinations = generate_combinations(num_variables)

print_matrix(combinations, 1)
resp = results_truth_table(combinations)

for i in range(len(resp)):
    print(resp)


print(combinations)
