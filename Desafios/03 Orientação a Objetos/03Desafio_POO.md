# Sistema Bancário em POO

## Objetivo Geral
Iniciar a modelagem de um sistema bancário utilizando Programação Orientada a Objetos (POO). O projeto inclui a criação de classes para representar clientes e operações bancárias, como depósito e saque.

## Desafio
Atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML fornecido.

## Desafio Extra
Após concluir a modelagem das classes e a criação dos métodos, atualizar os métodos que tratam as opções do menu para funcionarem com as classes modeladas.

## Estrutura do Projeto

### Classes

- **Cliente**
  - Atributos:
    - `endereco`: Endereço do cliente.
    - `contas`: Lista de contas associadas ao cliente.
  - Métodos:
    - `realizar_transacao(conta, transacao)`: Realiza uma transação em uma conta.
    - `adicionar_conta(conta)`: Adiciona uma conta à lista de contas do cliente.

- **PessoaFisica** (herda de Cliente)
  - Atributos:
    - `nome`: Nome do cliente.
    - `data_nascimento`: Data de nascimento do cliente.
    - `cpf`: CPF do cliente.

- **Conta**
  - Atributos:
    - `_saldo`: Saldo da conta.
    - `_numero`: Número da conta.
    - `_agencia`: Agência da conta.
    - `_cliente`: Cliente associado à conta.
    - `_historico`: Histórico de transações da conta.
  - Métodos:
    - `sacar(valor)`: Realiza um saque na conta.
    - `depositar(valor)`: Realiza um depósito na conta.

- **ContaCorrente** (herda de Conta)
  - Atributos:
    - `limite`: Limite de saque.
    - `limite_saques`: Limite de saques.
  - Métodos:
    - `sacar(valor)`: Realiza um saque na conta corrente.

- **Historico**
  - Atributos:
    - `transacoes`: Lista de transações.
  - Métodos:
    - `adicionar_transacao(transacao)`: Adiciona uma transação ao histórico.

- **Transacao** (classe abstrata)
  - Métodos:
    - `valor`: Retorna o valor da transação.
    - `registrar(conta)`: Registra a transação em uma conta.

- **Saque** (herda de Transacao)
  - Atributos:
    - `_valor`: Valor do saque.
  - Métodos:
    - `registrar(conta)`: Registra o saque em uma conta.

- **Deposito** (herda de Transacao)
  - Atributos:
    - `_valor`: Valor do depósito.
  - Métodos:
    - `registrar(conta)`: Registra o depósito em uma conta.

### Menu do Sistema

O menu do sistema foi atualizado para funcionar com as classes modeladas. Ele permite realizar as seguintes operações:

- Depositar
- Sacar
- Exibir Extrato
- Criar Novo Cliente
- Criar Nova Conta
- Listar Contas
- Sair

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo principal do projeto:
   ```bash
   python main.py
