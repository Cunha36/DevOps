menu = """ 

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMTE_SAQUES = 3  

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Dgite o valor que será depositado R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${saldo:.2f}\n" 

        else:
            print("Operação falho! valor informado é inválido.")

    elif opcao == "s":

        valor = float(input("Digite o valor que será sacado R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMTE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou, o valor de saques excedeu o limite.")

        elif excedeu_saques:
            print("Operação falhou, o número máximo de saques foi excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(extrato)

        else:
            print("Operação falhou! o valor informado é inválido. ")
        
    elif opcao == "e":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================================")
    
    elif opcao == "q":
        break

    else:
        print("Opção inválida, selecione novamente a opção desejada")
