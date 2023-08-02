# Ao digitar um número, retornará o fatorial desse número

def fatorial(x,a,n):
    
    x = x*a
    a=a-1
    if a >= 2:
        return fatorial(x,a,n)
    else:
        print(f"{n}! = {x}")


x = int(input("Digite um número: "))
if x == 1:
    print(1)
else:
    fatorial(x,x-1,x)