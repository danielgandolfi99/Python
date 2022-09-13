def main():
    for num in range(1000,2001):
        resto = num % 11
        if resto == 2:
            print(num)

main()