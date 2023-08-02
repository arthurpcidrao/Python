# Digite um número e tenha a sequência fibonacci

fib = []
fib.append(0)
fib.append(1)

def sequencia_fibonacci(x,i):
    fib.append(fib[i-1] + fib[i-2])
    if (x == 1):
        return print(f"{fib[i]}", end="\n")
    else:
        print(f"{fib[i]}", end=" ")
        i=i+1
        x=x-1
        return sequencia_fibonacci(x,i)

n = int(input("Digite quantos números você quer receber da sequência: "))

print(f"Fib[{n}] =", end = ' ')

if (n==1):
    print(0)

elif(n==2):
    print(1)

elif (n>2):
    print(f"0 1", end=" ")
    sequencia_fibonacci(n-2,2)
