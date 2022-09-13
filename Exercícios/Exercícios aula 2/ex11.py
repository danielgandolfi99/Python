def main():
    loop_notas()
    medias_notas()
    notas_acima()
    mensagens()

def loop_notas():
    global notas, acima, abaixo, soma, cont, n
    notas = []
    acima = []
    abaixo = []
    soma = 0
    cont = 0
    n = float(input('Digite a nota: '))
    while n != -1:
        notas.append(n)
        soma += n
        cont = cont + 1
        notas_abaixo()
        n = float(input('Digite a nota: '))

def medias_notas():
    global media_notas
    media_notas = soma / cont

def notas_reverso():
    print(notas)
    for i in (notas[::-1]):
        print(i)

def notas_acima():
    for n in notas:
        if n > media_notas:
            acima.append(n)

def notas_abaixo():
    if n < 7:
        abaixo.append(n)

def aprovacao():
    if media_notas >= 7:
        print(f'O ALUNO FOI APROVADO')
    else:
        print(f'O ALUNO FOI REPROVADO')

def mensagens():
    print(f'A quantidade de notas lidas foi de: {cont}')
    notas_reverso()
    print(f'A soma de todas as notas foi de: {soma}')
    print(f'A média geral das notas foi de: {media_notas}')
    print(f'As notas acima da média geral foram: {acima}')
    print(f'As notas abaixo da média 7 foram: {abaixo}')
    aprovacao()

main()
