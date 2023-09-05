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
    
    input_formula = remove_space(input_formula)
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

# Função para verificar caracteres
def check_denial(s):
    # Itera através da expressão começando do segundo caractere
    for i in range(1, len(s)):
        # Verifica se o caractere atual é um operador lógico e o anterior é uma negação "~"
        if s[i] in ["V", "∧", "^", "→", "↔", "v"] and s[i - 1] == "~":
            return False  # Se o caractere e til forem consecutivos , retorna Falso
    
    return True  # Se não for encontrada a ocasião, retorna Verdadeiro


# Função para verificar se a expressão está correta com base nas verificações
def check_correct_expression(s):
    # Chama as funções check_sequence e check_denial
    # Se ambas retornarem Verdadeiro, a expressão está correta; caso contrário, está incorreta
    if check_sequence(s) and check_denial(s):
        return True
    else:
        return False

def double_negation(string):
    resultado = []
    i = 0
    while i < len(string):
        if string[i] == "~":
            # Verifica se o próximo caractere também é "~"
            if i + 1 < len(string) and string[i + 1] == "~":
                # Avança dois caracteres para remover ambos
                i += 2
            else:
                # Adiciona apenas um "~" ao resultado
                resultado.append(string[i])
                i += 1
        else:
            # Adiciona o caractere atual ao resultado
            resultado.append(string[i])
            i += 1
    # Converte a lista de caracteres de volta para uma string
    return "".join(resultado)

def correction_parentheses(input_str):
    output_str = ""
    i = 0
    
    while i < len(input_str):
        if input_str[i] == '(':
            j = i + 1
            while j < len(input_str) and input_str[j] == '~':
                j += 1
            
            k = j
            while k < len(input_str) and input_str[k].isalpha() and input_str[k] in alphabet:
                k += 1
            
            if k < len(input_str) and input_str[k] == ')':
                output_str += input_str[i+1:k]  # Exclui os parênteses
                i = k + 1
            else:
                output_str += input_str[i]
                i += 1
        else:
            output_str += input_str[i]
            i += 1
    
    return output_str

def distribute(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i] == "~" and i + 1 < len(text) and text[i + 1] == "(":
            i += 2  # Avança além de "~("
            open_parentheses = 1
            j = i
            while j < len(text):
                if text[j] == "(":
                    open_parentheses += 1
                elif text[j] == ")":
                    open_parentheses -= 1
                    if open_parentheses == 0:
                        break
                j += 1
            if j < len(text):
                content_within_parentheses = text[i:j]  # Exclui o parêntese de fechamento
                allowed_operators = "v∧^→↔()"
                for c in content_within_parentheses:
                    if c == "~":
                        result += c  # Mantenha a negação
                    elif c not in allowed_operators:
                        result += "~" + c  # Adicione uma negação antes de outros caracteres
                    else:
                        result += c
                i = j + 1
            else:
                # Não encontrou o parêntese de fechamento, apenas copia o texto original
                result += text[i - 2:i]  # Inclui "~("
                i += 2
        else:
            result += text[i]
            i += 1
    return result

def formatting_parentheses(input_str):
    output_str = ""
    i = 0
    
    while i < len(input_str):
        if input_str[i] == '~':
            j = i + 1
            while j < len(input_str) and input_str[j].isalpha() and input_str[j] in alphabet:
                j += 1
            
            if j > i + 1:  # Se encontrou uma letra após "~"
                output_str += f'({input_str[i:j]})'
                i = j
            else:
                output_str += input_str[i]
                i += 1
        else:
            output_str += input_str[i]
            i += 1
    
    return output_str

def letras_duplicadas(equation):
    test = True
    i = 0
    while (i < len(equation) - 1):
        j = 0
        while (j < len(alphabet)):
            k = 0
            while(k < len(alphabet)):
                if (equation[i] == alphabet[j] and equation[i+1] == alphabet[k]):
                    test = False
                k = k + 1
            j = j + 1
        i = i + 1

    return test


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
    
    if ((var > 1) and (var>simb)):
        operacao.append(parcial_equation)
    elif(neg > 0):
        operacao.append(parcial_equation)

    return equation, operacao



n = 1
while(n != 2):

    equation = input("Digite uma equação lógica: ")

    equation = remove_space(equation)
    equation = correction_parentheses(equation)
    equation = distribute(equation)
    equation = double_negation(equation)
    equation = formatting_parentheses(equation)
    equation_s = equation

    print()

    equacao_valida = bool(lexical_analysis(equation) and is_well_formed_formula(equation) and check_correct_expression(equation) and letras_duplicadas(equation))

    if(equation == '' or equation[-1] == ''):
        equacao_valida = False

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