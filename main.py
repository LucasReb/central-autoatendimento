import os

#Import das funções para cada operação
from novopedido import novo_pedido
from cancelar import cancelar_pedido
from inserir import inserir_produto
from cancelar_produto import cancelar_produto
from valor import verificar_valor
from extrato import extrato

while True:
    print("Menu Inicial\n")
    #Print utilizado para representar menu incial
    print(      
            "1 - Novo pedido \n"
            "2 - Cancelar pedido \n"
            "3 - Inserir produto \n"
            "4 - Cancelar produto\n"
            "5 - Valor do pedido \n"
            "6 - Extrato do pedido \n\n"
            "0 - Sair")

    #Seleção de uma área do menu
    op = int(input())

    #Operação de realizar novo pedido quand o cpf é novo
    if op == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Chamada função novo pedido
        novo_pedido()
    #Operação para cancelar um pedido existente
    elif op == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Chamada função cancelar pedido
        cancelar_pedido()
    #Operação para inserir pedido
    elif op == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Chamada função inserir pedido
        inserir_produto()
    #Operação para cancelar produto    
    elif op == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Chamada função cancelar pedido
        cancelar_produto()
    elif op == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Chamada função para exibir valor
        verificar_valor()
    elif op == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Chamada função extrato
        extrato()
    #Operação para sair do programa
    elif op == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        break 

    #Condicional que identifica operações inválidas
    if type(op) != int or op < 0 or op > 6:
        print("Operação inválida, digite uma operação válida! \n")