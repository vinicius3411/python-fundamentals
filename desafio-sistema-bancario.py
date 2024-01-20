# criar um sistema bancário com depósito, saque e extrato apenas um usuário então não precisa de conta e senha
# Todos os depósitos devem ser armazenados em uma variavel e exibidos na operação extrato
# todos os depósitos devem ser numeros positivos
# o sistema deve permitir até 3 saques diários com um limite de 500 por saque
# caso o usuário não tenha saldo para sacar o dinheiro, o sistema deve avisar que não há saldo e não realizar o saque
# todos os saques devem ficar armazenados em uma variável para que sejam exibidos na operação extrato
# todos os valores em extrato devem estar em R$ e na listagem do extrato deve constar o salto atual da conta

menu = '''

========== Menu ==========

Selecione a opção desejada

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

saldo = round(0, 2)
historico_depositos = []
historico_saques = []
limite_saque = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        deposito = float(input('Digite o valor que deseja depositar: '))
        if deposito <= 0:
            print('Operação não realizada, retornando ao menu principal.')
        else:
            saldo += deposito
            historico_depositos.append(deposito)
            print('Depósito efetuado com sucesso, retornando ao menu principal.')

    elif opcao == '2':
        # Verifica se o número máximo de saques por sessão foi atingido
        if numero_saques >= LIMITE_SAQUES:
            print("Limite máximo de saques por sessão atingido.")
        else:
            # Solicita o valor do saque ao usuário
            saque = float(input('Digite o valor que deseja sacar: '))

            # Verifica se o valor do saque não ultrapassa o limite por saque
            if saque > limite_saque:
                print(
                    f"Limite máximo de saque por operação é de R$ {limite_saque:.2f}.")
            else:
                # Verifica se o saldo é suficiente
                if saque <= 0 or saldo < saque:
                    print('Operação não realizada, saldo insuficiente.')
                else:
                    # Atualiza o saldo
                    saldo -= saque
                    historico_saques.append(saque)
                    numero_saques += 1
                    print(f'Saque de R$ {saque:.2f} realizado com sucesso.')

    elif opcao == '3':
        print(f'''
Seu saldo é de: R$ {saldo:,.2f}

Histórico de depósitos:''')
        # Itera sobre o histórico de depósitos e imprime cada valor formatado
        for deposito in historico_depositos:
            print(f'R$ {deposito:,.2f}')

        print('Histórico de saques:')
        # Itera sobre o histórico de saques e imprime cada valor formatado
        for saque in historico_saques:
            print(f'R$ {saque:,.2f}')

    elif opcao == '0':
        break

    else:
        print('Operação inválida, por favor selecione a operação desejada.')
