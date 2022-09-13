n = int(input('Digite a quantidade de números: '))
maior = 0
menor = 0
for n in range(1,n):
    numero = int(input('Digite o número: '))
    if n == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('O maior número lido é: ',maior)
print('O menor número lido é: ',menor)

