def main():
    pessoas = []
    idades = []
    alturas = []
    soma = 0
    alta = 0
    cont = 0
    for i in range(3):
        pessoa = []
        idade = int(input(f'Digite a idade {i + 1} : '))
    #    peso = float(input(f'Digite o peso {i + 1} em kg: '))
        altura = float(input(f'Digite a altura {i + 1}: '))
        pessoa.append(idade)
        idades.append(idade)
    #    pessoa.append(peso)
        pessoa.append(altura)
        alturas.append(altura)
        pessoas.append(pessoa)
    for n in idades:
        soma = soma + n
    for x in alturas:
        if x > 1.90:
            cont = cont + 1
            for c in idades:
                if c >= 10 and c <= 30:
                    alta = alta + 1
    print(alta)
    print(cont)
    porcentagem_altura = (alta / cont) * 100
    media_idades = soma / len(idades)
    print(f'A porcentagem das alturas é de: {porcentagem_altura}%')
    print(f'A media das idades é de: {media_idades}')
    #print(pessoas)


main()