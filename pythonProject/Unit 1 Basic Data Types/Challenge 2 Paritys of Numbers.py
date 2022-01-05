def checkParity(n):
    parity = (n % 2)
    if parity == 0:

        result = 0

    else:
        result = 1

    return result


result = checkParity(5)
print(result)
