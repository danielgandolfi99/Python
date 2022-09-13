def main():
    langs = ["HTML", "CSS", "Python", "JavaScript"]
    nome = input('Digite o nome: ')
    existe = False
    for i in langs:
        if i == nome:
           existe = True
    print(existe)

main()