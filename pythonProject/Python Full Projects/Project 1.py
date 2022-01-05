import random


def guess(x):

    random_number = random.randint(1, x)

    guess = 0

    while guess != random_number:
        guess = int(input(f"Adivina un numero desde 1 a {x}: "))

        if guess < random_number:
            print("Lo siento, muy bajo.")

        elif guess > random_number:
            print("Lo siento, muy alto")

    print("Felicidades adivinaste el numero")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'y':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Es {guess} muy alto (A), muy bajo (B), o Correcto (Y)??: ").lower()
        if feedback == 'a':
                high = guess - 1
        elif feedback == 'b':
                low = guess + 1

    print(f'parece que la compu adivino el numero, {guess}, paja')


computer_guess(10)