import os

def cancelar_pedido():
    print("\nCancelar pedido")

    #Requisição de dados do usuário
    documento = int(input("Digite seu CPF: "))
    senha = input("Digite sua senha: ")

    if os.path.exists(f'{documento}.txt'):
        arq = open(f'{documento}.txt', 'r')
        linha = arq.readlines()
        arq.close()
        if str(senha) + '.\n' in linha:
            os.system('cls' if os.name == 'nt' else 'clear')
            os.remove(f'{documento}.txt')
            os.remove(f'extrato_{documento}.txt')
            print("Pedido cancelado com sucesso!")
        else:
            print("Senha incorreta!\n")
    else:
        print("CPF não cadastrado!\n")   