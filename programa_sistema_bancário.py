
menu = ('''
    
    ***************************
    Escolha a opção desejada: 
    ***************************

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    ***************************

''')

saque = 0
deposito = 0
saldo = 0
extrato = []
#ex_saque = []
numero_saques = 0


while True:

    opcao = input(menu)
    

    if opcao == 'd':
        deposito = (int(input('Qual o valor que deseja depositar: R$ ')))
        saldo+=deposito
        extrato.append({'Depósito': deposito})
        print(extrato)   
        if deposito <= 0:
            print('Não é possível depositar esse valor!')
        else:
            print(f' O valor de R$ {deposito} foi incluido na sua conta')
            print(f'Você tem R$ {saldo} na sua conta!')
            
        
    elif opcao == 's':
        saque = (int(input('Qual o valor valor deseja sacar: R$ ')))
        numero_saques+=1
        if numero_saques >= 4:
            print('Não é possível realizar mais que 3 saques por dia!')
        elif saque > saldo:
            print('Não será possível sacar o dinheiro por falta de saldo!')
        elif saque > 500:
            print('Não é possivel retirar esse valor!')
        elif saque <= 0:
            print('não é possível sacar esse valor!')
        else:
            extrato.append({'Saque': saque})
            saldo-=saque
            print(f'O valor de R$ {saque} foi retirado!')
            print(f'Você tem R$ {saldo} na sua conta!')
            print(extrato)
            
            
    elif opcao == 'e':
        if extrato == 0:
            extrato = print('Não foram realizadas movimentações!')
        else:
            #for extrato in extrato:
            for extrato in extrato:
                print(extrato)

            print(f'\033[31mVocê tem R$ {saldo:.2f} na sua conta!\033[m')




    elif opcao == 'q':
        break

    else:
        print('Operação inválida, selecione novamente a operação desejada.')

    


