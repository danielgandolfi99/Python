def main():
    calcula_media()
    verifica_situacao()
    print(f'Suas notas foram: {notas}')
    print(f'A media das notas foi de: {media_notas}')

def calcula_media():
    global notas
    global media_notas
    notas = []
    for n in range(4):
        notas.append(float(input('Digite as notas do aluno: ')))
    soma = 0
    for nota in notas:
        soma += nota
        media_notas = soma / 4

def verifica_situacao():
    if media_notas >= 7:
        print('APROVADO')
    else:
        print('REPROVADO')
main()