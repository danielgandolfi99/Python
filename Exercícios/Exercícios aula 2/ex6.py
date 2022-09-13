def main():
    pessoas = ["John", "Joseph", "Rebecca", "Alex", "Lily", "Neil", "Eddie", "Susan", "David"]
    letras = str(input('Digite duas letras: '))
    var = 0
    for i in pessoas:
        if letras == i[:2]:
            print(i)
            var = 1
    if var == 0:
        print('Nome não existente')
main()