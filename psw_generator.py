from random import choice
from string import ascii_letters, digits


def rand_psw():
    psw = []
    for num in range(0, 4):
        psw.append(f'{choice(ascii_letters)}{choice(digits)}{choice(ascii_letters)}{choice(digits)}')
    return '-'.join(psw)


if __name__ == '__main__':
    print(rand_psw())
