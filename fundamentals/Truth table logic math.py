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
    aux = 0
    i = 0
    sum_enter = 0
    sum_out = 0
    sum_gen = sum_enter + sum_out
    
    while (aux != 1):

        if (equation_m[i] == '(' ):
            sum_enter = sum_enter + 1
            j = i
            while(aux != 1):
                if (equation_m[j] == ')' ):
                    sum_out = sum_out + 1
                    break

                if (j == len(equation_m) - 1):
                    break
            if (sum_enter == sum_out):
                test = True
            else:
                test = False      

        elif (equation_m[i] == ')' ):
            sum_out = sum_out + 1
            if ((sum_enter == 0) and (sum_out > 0)):
                test = False

        if (i == len(equation_m) - 1):
            aux = 1        
    
    print(test)
        



#sentense = input("Digite uma frase: ")
equation = input("Digite uma equação lógica: ")

#sentense_analysis(sentense)
lexical_analysis(equation)

print(equation)