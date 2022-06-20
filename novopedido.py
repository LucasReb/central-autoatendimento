#Import bibliotecas externas
import os
from datetime import datetime

def novo_pedido():
    print("\nNovo pedido")

    #Requisição de dados do usuário
    nome = input("Digite seu nome: ")
    documento = int(input("Digite seu CPF: "))
    senha = input("Crie uma senha: ")

    #Comparação do nome de arquivos já inseridos com o cpf inserido
    if os.path.exists(f'{documento}.txt') == True:
        print()
        os.system('cls' if os.name == 'nt' else 'clear')
        #Informa que o CPF já está cadastrado
        print("CPF já cadastrado, digite um CPF válido.\n")
        #Volta ao menu principal
        exec(open('main.py').read())  
    else:
        #Abre um arquivo nomeado com o documento do usuário
        arq_user = open(f'{documento}.txt', 'a', encoding="utf-8")
        #Escreve as variaveis no arquivo destinada ao usuario
        arq_user.write(senha + '.\n')
        
        #Abrir arquivo de extrato do usuário
        ext_user = open(f'extrato_{documento}.txt', 'w', encoding="utf-8")

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("Cliente cadastrado com sucesso!\n")

        #Escreve as informações do usuário e do pedido no arquivo de extrato
        ext_user.write("Nome: {0}\nCPF: {1}\nData: {2}\nItens do pedido: \n".format(nome, str(documento), str(datetime.today().strftime('%Y-%m-%d %H:%M'))))

        total = []
        #Abre espaço para inserir a quantidade de cada produto
        prod1 = []
        prod2 = []
        prod3 = []
        prod4 = []
        prod5 = []
        prod6 = []
        prod7 = []

        #Executa o menu de pedidos
        while True:    
            #Menu de pedidos
            print("""Código     | Produto              | Preço
           |                      |      
    1      | X-salada             | R$ 10,00
    2      | X-burguer            | R$ 10,00
    3      | Cachorro quente      | R$ 7,50
    4      | Misto quente         | R$ 8,00
    5      | Salada de frutas     | R$ 5,50
    6      | Refrigerante         | R$ 4,50
    7      | Suco natural         | R$ 6,25 \n""")

            #Pergunta ao usuário o produto e quantidade que ele deseja inserir no seu pedido
            codigo_produto = input("Digite o código do produto desejado: ")
            quantidade_produto = int(input("Digite a quantidade desejada: "))

            #Condicionais que verificam o código do produto solicitado
            if codigo_produto == "1":
                valor = quantidade_produto * 10.00
                qnt_prod1 = quantidade_produto * 1
                qnt_prod2 = 0
                qnt_prod3 = 0
                qnt_prod4 = 0
                qnt_prod5 = 0
                qnt_prod6 = 0
                qnt_prod7 = 0
                ext_user.write("X-salada         | Quantidade: %i | Preço unitário: R$ 10,00 | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
            elif codigo_produto == "2":
                valor = quantidade_produto * 10.00
                qnt_prod2 = quantidade_produto * 1
                qnt_prod3 = 0
                qnt_prod4 = 0
                qnt_prod5 = 0
                qnt_prod6 = 0
                qnt_prod7 = 0
                qnt_prod1 = 0
                ext_user.write("X-burguer        | Quantidade: %i | Preço unitário: R$ 10,00 | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
            elif codigo_produto == "3":
                valor = quantidade_produto * 7.50
                qnt_prod3 = quantidade_produto * 1
                qnt_prod4 = 0
                qnt_prod5 = 0
                qnt_prod6 = 0
                qnt_prod7 = 0
                qnt_prod1 = 0
                qnt_prod2 = 0
                ext_user.write("Cachorro quente  | Quantidade: %i | Preço unitário: R$ 7,50  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
            elif codigo_produto == "4":
                valor = quantidade_produto * 8.00
                qnt_prod4 = quantidade_produto * 1
                qnt_prod5 = 0
                qnt_prod6 = 0
                qnt_prod7 = 0
                qnt_prod1 = 0
                qnt_prod2 = 0
                qnt_prod3 = 0
                ext_user.write("Misto quente     | Quantidade: %i | Preço unitário: R$ 8,00  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
            elif codigo_produto == "5":
                valor = quantidade_produto * 5.50
                qnt_prod5 = quantidade_produto * 1
                qnt_prod6 = 0
                qnt_prod7 = 0
                qnt_prod1 = 0
                qnt_prod2 = 0
                qnt_prod3 = 0
                qnt_prod4 = 0
                ext_user.write("Salada de frutas | Quantidade: %i | Preço unitário: R$ 5,50  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
            elif codigo_produto == "6":
                valor = quantidade_produto * 4.50
                qnt_prod6 = quantidade_produto * 1
                qnt_prod7 = 0
                qnt_prod1 = 0
                qnt_prod2 = 0
                qnt_prod3 = 0
                qnt_prod4 = 0
                qnt_prod5 = 0
                ext_user.write("Refrigerante     | Quantidade: %i | Preço unitário: R$ 4,50  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
            elif codigo_produto == "7":
                valor = quantidade_produto * 6.25
                qnt_prod7 = quantidade_produto * 1
                qnt_prod1 = 0
                qnt_prod2 = 0
                qnt_prod3 = 0
                qnt_prod4 = 0
                qnt_prod5 = 0
                qnt_prod6 = 0
                ext_user.write("Suco natural     | Quantidade: %i | Preço unitário: R$ 6,25  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
            else:
                print("Código inválido, insira um número válido! \n")
                break

            total.append(valor)
            prod1.append(qnt_prod1)
            prod2.append(qnt_prod2)
            prod3.append(qnt_prod3)
            prod4.append(qnt_prod4)
            prod5.append(qnt_prod5)
            prod6.append(qnt_prod6)
            prod7.append(qnt_prod7)

           #Confirmação para saber se usuário quer inserir outro produto ao seu pedido
            novo_produto = input("Deseja adicionar outro produto? (S/N)")

            if novo_produto == "S" or novo_produto == "s":
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
                
        ext_user.close() 

    total_final = sum(total)
    arq_user.write(str(total_final) + '\n')

    num_prod1 = sum(prod1)
    arq_user.write(str(num_prod1) + '\n')

    num_prod2 = sum(prod2)
    arq_user.write(str(num_prod2) + '\n')

    num_prod3 = sum(prod3)
    arq_user.write(str(num_prod3) + '\n')

    num_prod4 = sum(prod4)
    arq_user.write(str(num_prod4) + '\n')

    num_prod5 = sum(prod5)
    arq_user.write(str(num_prod5) + '\n')

    num_prod6 = sum(prod6)
    arq_user.write(str(num_prod6) + '\n')

    num_prod7 = sum(prod7)
    arq_user.write(str(num_prod7) + '\n')

    #Fecha arquivos 
    arq_user.close()