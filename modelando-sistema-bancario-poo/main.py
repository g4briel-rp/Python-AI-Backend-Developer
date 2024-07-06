from abc import ABC, abstractmethod
import os

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0.0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero_conta, cliente):
        return cls(numero_conta, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor >= 0.0:
            if self._saldo >= valor:
                self._saldo -= valor
                print("Saque realizado.")
                return True
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido.")
        
        return False

    def depositar(self, valor):
        if valor > 0.0:
            self._saldo += valor
            print("Depósito realizado.")
            return True
        else:
            print("Valor inválido.")

        return False
    
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500.0, limite_saques=3):
        super().__init__(numero_conta, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saque = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])
        if numero_saque < self._limite_saques:
            if valor <= self._limite:
                return super().sacar(valor)
            else:
                print("Valor de saque acima do limite.")
        else:
            print("Limite de saques atingido.")
        
        return False

    def __str__(self):
        return f"""\
            Cliente: {self.cliente.nome}
            Agência: {self.agencia}
            Número da conta: {self.numero_conta}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.tipo,
            "valor": transacao.valor

        })

class Transacao(ABC):
    @property
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._tipo = "Saque"
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @property
    def tipo(self):
        return self._tipo

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._tipo = "Depósito"
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @property
    def tipo(self):
        return self._tipo

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

def ver_menu():
    menu = """
    BEM VINDO AO BANCO PYTHON DO BRASIL

    Escolha uma opção:
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [cl] - Criar Cliente
    [c] - Criar Conta
    [lc] - Listar Contas
    [q] - Sair

    => """

    return input(menu)

def operacao(clientes, tipo_operacao):
    cpf = input("Digite o CPF do cliente, somente os números: ")
    
    cliente_selecionado = verifica_cliente(clientes, cpf)
    if not cliente_selecionado:
        print("Cliente não encontrado. Operação inválida!")
        return
    
    if tipo_operacao == 'saque':
        valor = float(input("Digite o valor para saque: "))
        transacao = Saque(valor)
    elif tipo_operacao == 'deposito':
        valor = float(input("Digite o valor para depósito: "))
        transacao = Deposito(valor)

    conta_selecionada = selecionar_conta(cliente_selecionado)
    if not conta_selecionada:
        print("Conta não encontrada. Operação inválida!")
        return
    
    cliente_selecionado.realizar_transacao(conta_selecionada, transacao)

def verifica_cliente(clientes, cpf):
    filtragem_cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return filtragem_cliente[0] if filtragem_cliente else None

def selecionar_conta(cliente):
    if not cliente.contas:
        print("Cliente não possui contas.")
        return 
    
    listar_contas_cliente(cliente)

    numero_conta = int(input("Digite o número da conta: "))

    conta_selecionada = [conta for conta in cliente.contas if conta.numero_conta == numero_conta]
    return conta_selecionada[0] if conta_selecionada else None

def listar_contas_cliente(cliente):
    for conta in cliente.contas:
        print(f"Conta: {conta.numero_conta}")

def exibir_extrato(clientes):
    cpf = input("Digite o CPF do cliente, somente os números: ")
    
    cliente_selecionado = verifica_cliente(clientes, cpf)
    if not cliente_selecionado:
        print("Cliente não encontrado. Operação inválida!")
        return
    
    conta_selecionada = selecionar_conta(cliente_selecionado)
    if not conta_selecionada:
        print("Conta não encontrada. Operação inválida!")
        return
    
    transacoes = conta_selecionada.historico.transacoes
    
    print(f"\nEXTRATO DA CONTA {conta_selecionada.numero_conta} DO USUÁRIO {cliente_selecionado.nome}".center(20, "-"))
    if not transacoes:
        print("Não há movimentações cadastradas para esta conta.")
    else:
        for transacao in transacoes:
            print(f"{transacao['tipo']} de R$ {transacao['valor']:.2f}")
        print(f"saldo atual: R$ {conta_selecionada.saldo:.2f}")

def criar_cliente(clientes):
    cpf = input("Digite o CPF do cliente, somente os números: ")
    
    cliente_selecionado = verifica_cliente(clientes, cpf)
    if cliente_selecionado:
        print("CPF já cadastrado. Operação inválida!")
        return
    
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (dd-mm-aaaa): ")
    endereco = input(f"Digite o endereço do cliente, (logradouro, número - bairro - cidade/sigla do estado): ")

    novo_cliente = PessoaFisica(endereco=endereco, cpf=cpf, nome=nome, data_nascimento=data_nascimento)
    clientes.append(novo_cliente)

    print("Cliente cadastrado com sucesso.")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o CPF do cliente, somente os números: ")
    
    cliente_selecionado = verifica_cliente(clientes, cpf)
    if not cliente_selecionado:
        print("Cliente não encontrado. Operação inválida!")
        return
    
    nova_conta = ContaCorrente.nova_conta(cliente=cliente_selecionado, numero_conta=numero_conta)
    contas.append(nova_conta)
    cliente_selecionado.contas.append(nova_conta)

    print(f"Conta {nova_conta.numero_conta} criada com sucesso.")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(str(conta))

if __name__ == "__main__":
    clientes = []
    novo_cliente = PessoaFisica(endereco="cataguases", cpf='13407719698', nome='gabriel', data_nascimento='23-07-1999')
    clientes.append(novo_cliente)
    contas = []

    while True:
        opcao = ver_menu()
        os.system("cls")

        if opcao == "d":
            operacao(clientes, 'deposito')
        elif opcao == "s":
            operacao(clientes, 'saque')
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "cl":
            criar_cliente(clientes)
        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida.")
        
        input("Pressione Enter para continuar...")
        os.system("cls")