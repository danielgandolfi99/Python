def main():
    n = []
    num = int(input('Digite um número: '))
    n.append(num)
    num = int(str(num)[::-1])
    print(num)

main()