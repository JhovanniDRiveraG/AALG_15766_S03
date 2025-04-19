def resta(a,b):
    return a-b

def multiplicacion(a:int,b:int) -> int:
    return a*b


def saludo(a:str) -> str:
    x = "hola"+ a
    return x

def despedida(a:str) -> None:
    x = "chao"+ a
    print(x)

def mensaje(x):
    print("ALERTA:",x)




##
c = 5
d : int = 2
print(resta(5,2))
print(multiplicacion(5,2))
print(saludo("Carlos"))
despedida("Carlos")
mensaje("Enemigo acercan")

z = [(2*x)+1 for x in range(1,10+1)]

print(z)