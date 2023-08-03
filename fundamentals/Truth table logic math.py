def sentense_analysis (sentense):

    array = sentense.split(' ')
    i = 0
    for logica in (array):
        
        if (logica == "ou"):
            array[i] = 'v'
        i = i+1

    print(array)

def lexical_analysis (outracoisa):
    bp = 1


sentense = input("Digite uma frase: ")

sentense_analysis(sentense)