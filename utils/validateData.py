import os

def validateInt(msg:str) -> int:
    try:
        x = int(input(msg))
    except ValueError:
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validateInt(msg)
    else:
        return x

def validatetext(msg):
    x = input(msg)
    if all(c.isalpha() or c.isspace() for c in x):
        return x
    else:
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validatetext(msg)

def validateflot(msg:str) -> float:
    try:
        x = float(input(msg))
        return x
    except ValueError:
        print('Ingrese un valor válido')
        os.system("pause")
        return validateflot(msg)
