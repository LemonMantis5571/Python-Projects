def isDivisble(x, y):
    quotien, divi =  divmod(x,y)
    if (divi) == 0:
        return True
    else:
        return False

divi = isDivisble(10,5)
print(divi)