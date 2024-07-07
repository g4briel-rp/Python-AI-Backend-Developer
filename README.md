# Python AI Backend Developer

Estudos do curso Python AI Backend Developer

## 1. Desafio Sistema Bancário

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

- ### Especificações para a operação de Depósito

  Deve ser possível depositar valores positivos para a minha conta bancária/ A versão 1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

- ### Especificações para a operação de Saque

  O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500.00 por saque Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

- ### Especificações para a operação de Extrato

  Essa operação deve listar todos os depósitos e saques realizados na conta No fim da listagem deve ser exibido o saldo atual da conta Se o extrato estiver em branco, exibir a mensagem Não foram realizadas movimentações Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

## 2. Otimizando o Sistema Bancário com Funções Python

- ### Objetivo Geral

  Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

- ### Desafio

  Precisamos deixar nosso código mais modularizado, para isso vamos criar funçoes para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar contar corrente (vincular com o usuário).

- ### Separação em Funções

  Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor

- ### Saque

  A função saque deve receber os argumentos apenas por nome (keyword only).

- ### Depósito

  A função depósito deve receber os argumentos apenas por posição (positional only).

- ### Extrato

  A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).

- ### Criar Usuário (cliente)

  O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, número - bairro - cidada/sigla do estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

- ### Criar Conta Corrente

  O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

## 3. Modelando o Sistema Bancário em POO com Python

- ### Objetivo Geral

  Iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente e as operações bancárias: depósito e saque.

- ### Desafio

  Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O çódigo de seguir o modelo de classes UML a seguir:

  ![imagem](/imagens/Screenshot%202024-07-06%20105519.png)

- ### Desafio Extra

  Após concluir a modelagem das classes e a criação dos métodos, atualizar os métodos que tratam as opções do menu, para funcionarem com as classes modeladas.

## 4. Desafio da aula de "Decoradores, Iteradores e Geradores em Python"

## 5. Desafio da aula de "Lidando com Data, Hora e Fuso Horário no Python"
