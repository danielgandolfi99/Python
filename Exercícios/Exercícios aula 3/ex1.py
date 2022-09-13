def main():
    menu()

def menu():
    global cliente, clients, opcao
    clients = []
    opcao = 999
    while opcao != 0:
        print('Escolha a opção que deseja: ')
        print('1 - Adicionar clientes')
        print('2 - Buscar clientes por nome')
        print('3 - Excluir clientes')
        print('4 - Listar clientes')
        print('0 - Finalizar programa')
        opcao = int(input('Digite a opção desejada: '))
        menu0()
        menu1()
        menu2()
        menu3()
        menu4()
        invalido()

def menu1():
    if opcao == 1:
        conjunto = []
        cliente = input('Insira o nome do cliente: ')
        email = input('Digite o email do cliente: ')
        conjunto.append(cliente)
        conjunto.append(email)
        clients.append(conjunto)

def menu2():
    if opcao == 2:
        digitado = input('Digite o nome do cliente que deseja buscar: ')
        if clients == []:
            print('Nenhum cliente cadastrado')
            return menu()
        for name in clients:
            if digitado in name:
                print(name)
                break
        if digitado not in name:
            print('Cliente não encontrado')

def menu3():
    if opcao == 3:
        if clients == []:
            print('Nenhum cliente cadastrado')
        else:
            digitado = input('Digite o nome do cliente que deseja excluir: ')
            for name in clients:
                if digitado in name:
                    clients.remove(name)
                    print('Cliente excluído')
            if digitado not in name:
                print('Cliente não encontrado')

def menu4():
    if opcao == 4:
        if clients == []:
            print('Nenhum cliente cadastrado')
        for i in clients:
            print(i)

def menu0():
    if opcao == 0:
        print('Fechando aplicação...')

def invalido():
    if opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print('Opção inválida, digite novamente')

main()