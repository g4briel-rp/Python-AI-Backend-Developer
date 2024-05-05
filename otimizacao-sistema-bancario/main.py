import os

def add_user1(usuarios):
    usuario = dict(nome="Gabriel Ribeiro Passos", data_de_nascimento="23071999", cpf="13407719698", endereco="av guido marliere, 478 - haidee - cataguases/MG")
    usuarios["13407719698"] = usuario

def ver_menu():
    menu = """
    BEM VINDO AO BANCO PYTHON DO BRASIL

    Escolha uma opção:
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [u] - Criar Usuário
    [lu] - Listar Usuários
    [c] - Criar Conta
    [lc] - Listar Contas
    [luc] - Listar Contas do Usuário
    [q] - Sair

    => """

    return input(menu)

def informacoes_usuario(usuarios):
    menu = """"""

    for cpf, usuario in usuarios.items():
        menu += f"""
        Usuário {cpf}
        Nome: {usuario["nome"]}
        Data de Nascimento: {usuario["data_de_nascimento"][0:2]}/{usuario["data_de_nascimento"][2:4]}/{usuario["data_de_nascimento"][4:]}
        CPF: {usuario["cpf"][0:3]}.{usuario["cpf"][3:6]}.{usuario["cpf"][6:9]}-{usuario["cpf"][9:]}
        Endereço: {usuario["endereco"]}
        """

    return menu

def informacoes_contas(contas):
    menu = """"""

    for conta in contas:
        menu += f"""
        Conta {conta["numero_conta"]}
        Agência: {conta["agencia"]}
        Usuário: {conta["usuario"]}
        """

    return menu

def informacoes_contas_usuario(contas, cpf):
    menu = """"""

    for conta in contas:
        if conta["usuario"] == cpf:
            menu += f"""
            Número da conta {conta["numero_conta"]}
            Agência: {conta["agencia"]}
            Saldo: R$ {conta["saldo"]:.2f}
            Número de Saques: {conta["numero_saques"]}
            """

    return menu

def verifica_contas(contas, cpf):
    for conta in contas:
        if conta["usuario"] == cpf:
            return False

    return True

def verifica_cpf(usuarios, cpf):
    if cpf not in usuarios:
        return False
    
    return True

def verificar_existencia_conta(contas, numero_conta_selecionada, cpf):
    for conta in contas:
        if conta["usuario"] == cpf and conta["numero_conta"] == numero_conta_selecionada:
            return conta
        
    return None

def deposito(contas, usuarios, /):
    if len(contas) == 0:
        print("Não há contas cadastradas para realizar a operação. Por favor efetue a criação de uma conta. Operação inválida!")
        return

    cpf = input("Digite o CPF do usuário, somente os números: ")

    if not verifica_cpf(usuarios, cpf):
        print("Usuário não encontrado. Operação inválida!")
        return
    
    listar_contas_usuario(contas, usuarios, cpf)
    numero_conta_selecionada = int(input("Digite o número da conta que deseja realizar o depósito: "))

    conta_selecionada = verificar_existencia_conta(contas, numero_conta_selecionada, cpf)

    if conta_selecionada is None:
        print("Conta não encontrada. Operação inválida!")
        return

    valor_deposito = float(input("Digite o valor para depósito: "))
    
    if valor_deposito > 0:
        conta_selecionada["saldo"] += valor_deposito
        conta_selecionada["extrato"] += f"Depósito de R$ {valor_deposito:.2f} realizado.\n"
    else:
        print("Valor informado para deposito é um valor negativo. Operação inválida!")

def saque(*, contas, usuarios):
    if len(contas) == 0:
        print("Não há contas cadastradas para realizar a operação. Por favor efetue a criação de uma conta. Operação inválida!")
        return
    
    LIMITE_SAQUES = 3

    cpf = input("Digite o CPF do usuário, somente os números: ")

    if not verifica_cpf(usuarios, cpf):
        print("Usuário não encontrado. Operação inválida!")
        return
    
    listar_contas_usuario(contas, usuarios, cpf)
    numero_conta_selecionada = int(input("Digite o número da conta que deseja realizar o saque: "))
    
    conta_selecionada = verificar_existencia_conta(contas, numero_conta_selecionada, cpf)

    if conta_selecionada is None:
        print("Conta não encontrada. Operação inválida!")
        return

    valor_saque = float(input("Digite o valor para saque: "))

    if conta_selecionada["numero_saques"] < LIMITE_SAQUES:
        if valor_saque <= conta_selecionada["valor_limite_saque"]:
            if conta_selecionada["saldo"] >= valor_saque:
                conta_selecionada["saldo"] -= valor_saque
                conta_selecionada["numero_saques"] += 1
                conta_selecionada["extrato"] += f"Saque de R$ {valor_saque:.2f} realizado.\n"
            else:
                print("Saldo insuficiente. Operação inválida!")
        else:
            print(f"Valor informado para saque é acima do valor permitido de R$ {conta_selecionada["valor_limite_saque"]}. Operação inválida!")
    else:
        print("Você atingiu o limite de saques diários. Operação inválida!")

def extrato(contas, *, usuarios):
    if len(contas) == 0:
        print("Não há contas cadastradas para realizar a operação. Por favor efetue a criação de uma conta. Operação inválida!")
        return
    
    cpf = input("Digite o CPF do usuário, somente os números: ")

    if not verifica_cpf(usuarios, cpf):
        print("Usuário não encontrado. Operação inválida!")
        return
    
    listar_contas_usuario(contas, usuarios, cpf)
    numero_conta_selecionada = int(input("Digite o número da conta que deseja visualizar o extrato: "))
    
    conta_selecionada = verificar_existencia_conta(contas, numero_conta_selecionada, cpf)

    if conta_selecionada is None:
        print("Conta não encontrada. Operação inválida!")
        return
    
    print(f"\nEXTRATO DA CONTA {numero_conta_selecionada} DO USUÁRIO {cpf}".center(20, "-"))
    print(f"Não há movimentações cadastradas para esta conta." if not conta_selecionada["extrato"] else conta_selecionada["extrato"])

def criar_usuario(usuarios):
    nome = input(f"Digite o nome do usuário: ")
    data_de_nascimento = input(f"Digite a data de nascimento do usuário, somente os números: ")
    cpf = input(f"Digite o CPF do usuário, somente os números: ")

    if verifica_cpf(usuarios, cpf):
        print("CPF já cadastrado. Operação inválida!")
        return

    endereco = input(f"Digite o endereço do usuário, seguindo o padrão: logradouro, número - bairro - cidade/sigla do estado: ")

    usuario = dict(nome=nome, data_de_nascimento=data_de_nascimento, cpf=cpf, endereco=endereco)
    usuarios[cpf] = usuario
    print("Usuário cadastrado com sucesso!")

def listar_usuarios(usuarios):
    print(f"\nLISTA DE USUÁRIOS".center(20, "-"))
    print(f"Não há usuários cadastrados." if len(usuarios) == 0 else informacoes_usuario(usuarios))

def criar_conta(contas, usuarios):
    numero_conta = len(contas) + 1
    agencia = "0001"
    usuario = input("Digite o CPF do usuário: ")

    if usuario not in usuarios:
        print("Usuário não encontrado. Operação inválida!")
        return

    saldo = 0.0
    extrato = ""
    valor_limite_saque = float(input("Digite o valor limite para saque: "))
    numero_saques = 0

    conta = dict(numero_conta=numero_conta, agencia=agencia, usuario=usuario, saldo=saldo, extrato=extrato, valor_limite_saque=valor_limite_saque, numero_saques=numero_saques)
    contas.append(conta)
    print("Conta criada com sucesso!")

def listar_todas_contas(contas):
    print(f"\nLISTA DE CONTAS".center(20, "-"))
    print(f"Não há contas cadastradas." if len(contas) == 0 else informacoes_contas(contas))

def listar_contas_usuario(contas, usuarios, cpf):
    if not verifica_cpf(usuarios, cpf):
        print("Usuário não encontrado. Operação inválida!")
        return

    print(f"\nLISTA DE CONTAS DO USUÁRIO {cpf}".center(20, "-"))
    print(f"Não há contas cadastradas para este usuário." if verifica_contas(contas, cpf) else informacoes_contas_usuario(contas, cpf))

if __name__ == "__main__":
    usuarios = dict()

    # remover depois
    add_user1(usuarios)
    
    contas = []

    while True:
        opcao = ver_menu()
        os.system("cls")

        if opcao == "d":
            deposito(contas, usuarios)
        elif opcao == "s":
            saque(contas=contas, usuarios=usuarios)
        elif opcao == "e":
            extrato(contas, usuarios=usuarios)
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "lu":
            listar_usuarios(usuarios)
        elif opcao == "c":
            criar_conta(contas, usuarios)
        elif opcao == "lc":
            listar_todas_contas(contas)
        elif opcao == "luc":
            cpf = input("Digite o CPF do usuário, somente os números: ")
            listar_contas_usuario(contas, usuarios, cpf)
        elif opcao == "q":
            print("Obrigado por utilizar o Banco Python do Brasil!")
            break
        else:
            print("Opção inválida! Tente novamente.")

        input("Pressione Enter para continuar...")
        os.system("cls")