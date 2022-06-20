from fileinput import close
import os

def inserir_produto():
    print("\nInserir produto\n")

    #Requisição de dados do usuário
    documento = int(input("Digite seu CPF: "))
    senha = input("Digite sua senha: ")
   
    if os.path.exists(f'{documento}.txt'):
        arq = open(f'{documento}.txt', 'r')
        linha = arq.readlines()
        total =  linha[1]
        total_prod1 = linha[2]
        total_prod2 = linha[3]
        total_prod3 = linha[4]
        total_prod4 = linha[5]
        total_prod5 = linha[6]
        total_prod6 = linha[7]
        total_prod7 = linha[8]
        total = float(total)
        total_prod1 = int(total_prod1)
        total_prod2 = int(total_prod2)
        total_prod3 = int(total_prod3)
        total_prod4 = int(total_prod4)
        total_prod5 = int(total_prod5)
        total_prod6 = int(total_prod6)
        total_prod7 = int(total_prod7)
        arq.close

        if senha+".\n" in linha:       
                #Executa o menu de pedidoss
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

                        codigo_produto = input("Digite o código do produto desejado: ")
                        quantidade_produto = int(input("Digite a quantidade desejada: "))
                        
                        #Abrir arquivo de extrato do usuário
                        ext_user = open(f'extrato_{documento}.txt', 'a', encoding="utf-8")            

                        #Condicionais que verificam o código do produto solicitado
                        if codigo_produto == "1":
                                valor = quantidade_produto * 10.00
                                total += valor
                                total_prod1 += quantidade_produto
                                ext_user.write("X-salada         | Quantidade: %i | Preço unitário: R$ 10,00 | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
                        elif codigo_produto == "2":
                                valor = quantidade_produto * 10.00
                                total += valor
                                total_prod2 += quantidade_produto
                                ext_user.write("X-burguer        | Quantidade: %i | Preço unitário: R$ 10,00 | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
                        elif codigo_produto == "3":
                                valor = quantidade_produto * 7.50
                                total += valor
                                total_prod3 += quantidade_produto
                                ext_user.write("Cachorro quente  | Quantidade: %i | Preço unitário: R$ 7,50  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
                        elif codigo_produto == "4":
                                valor = quantidade_produto * 8.00
                                total += valor
                                total_prod4 += quantidade_produto
                                ext_user.write("Misto quente     | Quantidade: %i | Preço unitário: R$ 8,00  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
                        elif codigo_produto == "5":
                                valor = quantidade_produto * 5.50
                                total += valor
                                total_prod5 += quantidade_produto
                                ext_user.write("Salada de frutas | Quantidade: %i | Preço unitário: R$ 5,50  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
                        elif codigo_produto == "6":
                                valor = quantidade_produto * 4.50
                                total += valor
                                total_prod6 += quantidade_produto
                                ext_user.write("Refrigerante     | Quantidade: %i | Preço unitário: R$ 4,50  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
                        elif codigo_produto == "7":
                                valor = quantidade_produto * 6.25
                                total += valor
                                total_prod7 += quantidade_produto
                                ext_user.write("Suco natural     | Quantidade: %i | Preço unitário: R$ 6,25  | Valor: R$ +%.2f\n" %  (quantidade_produto, valor))
                        else:
                                print("Código inválido, insira um número válido! \n")

                        #Confirmação para saber se usuário quer inserir outro produto ao seu pedido
                        novo_produto = input("Deseja inserir outro produto? (S/N)")

                        if novo_produto == "S" or novo_produto == "s":
                                print()
                        else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break
                

                arq = open(f'{documento}.txt', 'w')
                arq.write(senha + '.\n')


                total_final = str(total)
                arq.write(total_final + '\n')

                arq.write(str(total_prod1) + '\n')

                arq.write(str(total_prod2) + '\n')

                arq.write(str(total_prod3) + '\n')

                arq.write(str(total_prod4) + '\n')

                arq.write(str(total_prod5) + '\n')

                arq.write(str(total_prod6) + '\n')

                arq.write(str(total_prod7) + '\n')        

                #Fecha arquivo do extrato
                ext_user.close()
                arq.close()
        else:
            print("Senha incorreta!\n")
    else:
        print("CPF não cadastrado!\n")   