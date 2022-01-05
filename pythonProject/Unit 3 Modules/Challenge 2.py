import math

def calculateSinCosTan(x):
    sine = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)

    return [sine,cos,tan]

[sine,cos,tan] = calculateSinCosTan(10)
print(sine,cos,tan)