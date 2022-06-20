import os

def extrato():
    print("\nExtrato\n")

    #Requisição de dados do usuário
    documento = int(input("Digite seu CPF: "))
    senha = input("Digite sua senha: ")

    if os.path.exists(f'{documento}.txt'):
      arq = open(f'{documento}.txt', 'r')
      linha = arq.readlines()
      arq.close()
      if senha+".\n" in linha:
        ext_user =  open(f'extrato_{documento}.txt', 'r', encoding="utf-8")
        data = ext_user.read()
        total = linha[1]
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n' + data)
        print("Total a pagar: R$ ", str(total))
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Senha incorreta!\n")
    else:
      print("CPF não cadastrado!\n")   
