def main():
    chocolate = float(input('Informe o preço do chocolate: '))
    fruta = float(input('Informe o preço da fruta: '))
    salgado = float(input('Informe o preço do salgado: '))
    if chocolate < fruta and chocolate < salgado:
        print(f'O produto que deve ser comprado é o chocolate! ')
    if fruta < chocolate and fruta < salgado:
        print(f'O produto que deve ser comprado é a fruta! ')
    if salgado < chocolate and salgado < fruta:
        print(f'O produto que deve ser comprado é o salgado! ')
    if chocolate == fruta == salgado:
        print(f'Todos os produtos tem o mesmo preço, faça sua escolha! ')
    if chocolate == fruta and chocolate < salgado:
        print(f'Chocolate e fruta possuem o mesmo preço! ')
    if chocolate == salgado and chocolate < fruta:
        print(f'Chocolate e salgado possuem o mesmo preço! ')
    if fruta == salgado and fruta < chocolate:
        print(f'Fruta e salgado possuem o mesmo preço! ')
        
main()