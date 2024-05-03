import os

if __name__ == "__main__":
    menu = """
    BEM VINDO AO BANCO PYTHON DO BRASIL

    Escolha uma opção:
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [q] - Sair

    => """
    
    saldo = 0.0
    valor_limite_saque = 500.0
    extrato = ""
    numero_saques = 0.0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)
        os.system("cls")

        if opcao == "d":
            valor_deposito = float(input("Digite o valor para depósito: "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito de R$ {valor_deposito:.2f} realizado.\n"
            else:
                print("Valor informado para deposito é um valor negativo. Operação inválida!")
        elif opcao == "s":
            valor_saque = float(input("Digite o valor para saque: "))
            if numero_saques < LIMITE_SAQUES:
                if valor_saque <= 500.0:
                    if saldo > valor_saque:
                        saldo -= valor_saque
                        numero_saques += 1
                        extrato += f"Saque de R$ {valor_saque:.2f} realizado.\n"
                    else:
                        print("Saldo insuficiente. Operação inválida!")
                else:
                    print("Valor informado para saque é acima do valor permitido de R$ 500,00. Operação inválida!")
            else:
                print("Você atingiu o limite de saques diários. Operação inválida!")
        elif opcao == "e":
            print("EXTRATO".center(20, "-"))
            if len(extrato) > 0:
                print(extrato)
            else:
                print("Nenhuma movimentação foi realizada ainda.")
            print(f"Saldo: R$ {saldo:.2f}")
        elif opcao == "q":
            print("Obrigado por utilizar o Banco Python do Brasil!")
            break
        else:
            print("Opção inválida! Tente novamente.")

        input("Pressione Enter para continuar...")
        os.system("cls")