import os

def verificar_valor():
  #Requisição de dados do usuário
  documento = int(input("Digite seu CPF: "))
  senha = input("Digite sua senha: ")

  while True: 
    if os.path.exists(f'{documento}.txt'):
          arq = open(f'{documento}.txt', 'r')
          linha = arq.readlines()
          if str(senha) + '.\n' in linha:
            total = linha[1]
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nTotal a pagar: R$", total)
            break
          else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Senha incorreta!\n")
            break
    else:
      print("CPF não cadastrado!\n")   
      break