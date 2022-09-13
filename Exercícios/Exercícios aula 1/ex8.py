import random
help(random)
n = int(input('Digite o número: '))
for n in range(0,n):
    numero = random.randint(1,50)
    print(numero)
