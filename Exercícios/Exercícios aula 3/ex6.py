def main():
    ano = int(input('Digite um ano: '))
    if ano % 4 == 0 and (ano % 400 == 0 or not ano % 100 == 0):
        print('Este ano é bissexto')
    else:
        print('Este ano não é bissexto')

main()