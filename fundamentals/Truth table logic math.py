def sentense_analysis (sentense):

    array = sentense.split(' ')
    i = 0
    for logic in (array):
        
        if (logic == "ou"):
            array[i] = 'v'
        i = i+1

    print(array)

def lexical_analysis (equation):
    alphabet = "abcdefghijklmnopqrstuvwxyzç ~^→↔()"
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

    verificacao(equation_m)


def verificacao (equation_m):
    # verificação do ():
    test = True
    sum_enter = 0
    sum_out = 0
    pares = 0
    pos_par_enter = []
    pos_par_out = []
    
    j = 0
    for letter in (equation_m):
        if (letter == '(' ):
            sum_enter = sum_enter+1
            pos_par_enter.append(j)

        if (letter == ')' ):
            sum_out = sum_out+1
            pos_par_out.append(j)
        
        j = j + 1
    
    if (sum_enter != sum_out):
        test = False
    
    else:
        num = sum_enter

        for i in range(num):
            if (pos_par_enter[i] < pos_par_out[num - 1 - i]):
                pares = pares + 1
        
        if (num == pares):
            test = True
        else:
            test = False
    
    print(test)
        



#sentense = input("Digite uma frase: ")
equation = input("Digite uma equação lógica: ")

#sentense_analysis(sentense)
lexical_analysis(equation)

print(equation)