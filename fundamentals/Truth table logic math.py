import ttg

alphabet_plus = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ vV∧~^→↔()"
alphabet = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
simbolos = "V∧~^→↔v"
simbolos_plus = "V∧~^→↔v()"



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



# Função para verificar uma sequência de símbolos permitidos
def check_sequence(s):
    allowed_symbols = ["V", "∧", "^", "→", "↔", "v"]

    # Itera através da expressão
    for i in range(len(s) - 1):
        # Verifica se o símbolo atual e o próximo estão em allowed_symbols
        if s[i] in allowed_symbols and s[i + 1] in allowed_symbols:
            return False  # Se uma sequência for encontrada, retorna Falso
    
    return True  # Se nenhuma sequência for encontrada, retorna Verdadeiro

# Função para verificar caracteres til consecutivos
def check_denial(s):
    # Itera através da expressão começando do segundo caractere
    for i in range(1, len(s)):
        # Verifica se o caractere atual e o anterior são ambos "~"
        if s[i] == "" and s[i - 1] == "":
            return False  # Se til consecutivos forem encontrados, retorna Falso
    
    return True  # Se nenhum til consecutivo for encontrado, retorna Verdadeiro

# Função para verificar se a expressão está correta com base nas verificações
def check_correct_expression(s):
    # Chama as funções check_sequence e check_denial
    # Se ambas retornarem Verdadeiro, a expressão está correta; caso contrário, está incorreta
    if check_sequence(s) and check_denial(s):
        return True
    else:
        return False



def analise (equation, operacao):
    pos_final = 0
    i = 0

    for var in (equation):
        if (var == ')' ):
            pos_final = i
            break
        i = i + 1
    
    if (pos_final == 0):
        
        parcial_equation = equation

    else:
        pos_inicial = 0
        i = 0
        for var in (equation[pos_final::-1]):  # iterando a equation de tras pra frente
            if (var == '(' ):
                pos_inicial = (len(equation[pos_final::-1]) - 1) - i
                break
            i = i + 1
    
        parcial_equation = equation[pos_inicial:pos_final+1]
    
    equation = equation.replace(parcial_equation, '')

    var = 0
    neg = 0
    simb = 0
    for i in parcial_equation:
        for j in alphabet:
            if (i == j):
                var = var+1
        for k in simbolos:
            if (i == k):
                simb = simb + 1
        if (i == '~'):
            neg = neg+1
    
    print(var)
    print(simb)
    print(neg)
    if ((var > 1) and (var>simb)):
        operacao.append(parcial_equation)
    elif(neg > 0):
        operacao.append(parcial_equation)
        

    return equation, operacao



n = 1
while(n != 2):

    equation = input("Digite uma equação lógica: ")

    equation = remove_space(equation)
    equation_s = equation

    print()

    equacao_valida = bool(lexical_analysis(equation) and is_well_formed_formula(equation) and check_correct_expression(equation))

    if (equacao_valida):
        variables = qtd_variables(equation)
        num_variables = len(variables)

        operacao = []
        operacoes = []

        while (equation != ''):
            equation, operacao = analise(equation, operacao)
        
        x = 0
        for i in equation_s:
            if ((i == '(' ) or (i == ')' ) ):
                x = x + 1
        if (x > 0):
            operacao.append(equation_s)
        print()

        for letter in operacao:
            for j in letter:
            
                if (j == 'v'):
                    letter = letter.replace('v', " or ")

                if (j == 'V'):
                    letter = letter.replace('V', " or ")

                if (j == '^'):
                    letter = letter.replace('^', ' and ')
                
                if (j == '∧'):
                    letter = letter.replace('∧', ' and ')
                
                if (j == '→'):
                    letter = letter.replace('→', ' => ')
                
                if (j == '↔'):
                    letter = letter.replace('↔', ' = ')
                
            operacoes.append(letter)

        print(ttg.Truths(variables,operacoes))

    else:
        print("\nA equação está errada, digite novamente!\n")

    print("Deseja continuar?\n (1) - SIM\n (2) - NÃO\n")
    n = int(input("Resposta: "))
    