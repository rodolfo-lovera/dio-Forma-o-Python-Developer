# Desafio: Otimizando Sistema Bancário com Funções Python

## Objetivo Geral
Separar as funções existentes de saque, deposito e extrato em funções. Criar duas novas funções? cadastrar usuário (cliente) e cadastrar conta bancária.

## Descrição
Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.

## Desafio

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções:criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

**1. Separação em funções:** Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

* **Operação de saque:** O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

* **Operação depósito:** A função depósito deve receber os argumentos apenas por posição (Positional only). Sugestão de argumentos: saldos, valor, extrato. Sugestão de retorno: saldo e extrato.

* **Operação extrato:** A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo; argumentos nomeados: extrato.

**2. Novas funções:** Precisamo criar duas novas funções: criar usuários e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

* **Criar usuário (cliente):** O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de dascimento, CPF e endereço. O endereço é uma string com o formato logradouro, número, bairro, cidade e estado(em sigla). Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

* **Criar conta corrente:**  O programa deve armazenas contas em uma lista, uma conta é composta por agência, número da conta e usuário. O número da conta é sequenvial, iniciado em 1. O número da agência é fixo: 0001. O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

