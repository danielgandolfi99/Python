def main():

    medias_diarias()
    media_geral()

def medias_diarias():
    temperaturas = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
    soma = 0
    media_dia = 0
    global medias_diarias
    medias_diarias = []

    for dia in temperaturas:
        for t in dia:
            soma += t
        media_dia = soma / len(dia)
        medias_diarias = medias_diarias + [media_dia]
    print(f'A media diária das temperaturas foi de: {medias_diarias}')

def media_geral():
    soma = 0
    for valor in medias_diarias:
        soma += valor
        geral = soma / len(medias_diarias)
    print(f'A media geral das temperaturas foi de: {geral} ')

main()