def main():
    idade1 = int(input('Digite a primeira idade: '))
    idade2 = int(input('Digite a segunda idade: '))
    idade3 = int(input('Digite a terceira idade: '))
    cont = 0
    if idade1 >= 18:
        cont = cont + 1
    if idade2 >= 18:
        cont = cont + 1
    if idade3 >= 18:
        cont = cont + 1
    print(f'A quantidade de pessoas maiores de idade é: {cont}')

main()