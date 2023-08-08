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
    
    equation = equation.replace(' ', '',count)
    print(equation)
        

#sentense = input("Digite uma frase: ")
equation = input("Digite uma equação lógica: ")

#sentense_analysis(sentense)
lexical_analysis(equation)