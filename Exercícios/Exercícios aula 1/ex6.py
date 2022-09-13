n = int
while n != 0:
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        print('O número {} é divisível por 2'.format(n))
    if n % 3 == 0:
        print('O número {} é divisível por 3'.format(n))
