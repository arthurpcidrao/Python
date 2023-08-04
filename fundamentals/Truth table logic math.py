def sentense_analysis (sentense):

    array = sentense.split(' ')
    i = 0
    for logic in (array):
        
        if (logic == "ou"):
            array[i] = 'v'
        i = i+1

    print(array)

def lexical_analysis (equation):
    alphabet = "abcdefghijklmnopqrstuvwxyz ~^→↔()"
    sum = 0

    for logic in (equation):
        for letter in (alphabet):
            if (logic == letter):
                sum = sum + 1

    if (sum == len(equation)):
        print("Os símbolos estão corretos")
    
    else:
        print("Os símbolos estão errados")


#sentense = input("Digite uma frase: ")
equation = input("Digite uma equação lógica: ")

#sentense_analysis(sentense)
lexical_analysis(equation)