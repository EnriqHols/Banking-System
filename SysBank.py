menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saque = 500
numero_de_saques = 0
LIMITE_DE_SAQUES = 3




while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato = (f"Depósito: R$ {valor: .2f}\n")

        else:
            print("Valor inválido")

    elif opcao == "2":
         valor = float(input("informe o valor do saque: "))

         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

         if excedeu_saldo:
             print("Saldo insuficiente")

         elif excedeu_limite:
             print("O valor do saque excede o limite")

         elif excedeu_saques:
             print("Você excedeu o número de saques")

         elif valor > 0:
             saldo -= valor
             extrato += (f"Saque: R$ {valor: .2f}\n")
             numero_de_saques += 1

         else:
            print("Valor inválido")

    elif opcao == "3":
        print("\n =============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\nSaldo: R$ {saldo: .2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Inválido")
        