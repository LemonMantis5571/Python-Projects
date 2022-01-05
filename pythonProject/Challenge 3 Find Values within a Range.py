def inRange(x, y):
    if x < 1 / 3 < y:
        resultado = True
    else:
        resultado = False

    return resultado


resultado = inRange(0, 4)

print(resultado)
