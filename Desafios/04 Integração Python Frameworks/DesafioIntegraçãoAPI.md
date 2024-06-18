# Desafio: Integração de Python com SQLite e MongoDB

Este repositório contém a resolução de um desafio de projeto que envolve a integração de Python com bancos de dados relacionais (SQLite) e não relacionais (MongoDB). O projeto é dividido em duas partes principais:

## Parte 1: Implementando um Banco de Dados Relacional com SQLAlchemy

### Objetivo
Implementar uma aplicação de integração com SQLite com base em um esquema relacional fornecido. Utilizar o esquema dentro do contexto de cliente e conta para criar as classes da API. Essas classes representam as tabelas do banco de dados relacional dentro da aplicação.

### Entregáveis
- Definição do esquema do banco de dados usando classes do SQLAlchemy.
- Inserção de um conjunto de dados mínimo para manipulação das informações.
- Execução de métodos de recuperação de dados via SQLAlchemy.

## Parte 2: Implementando um Banco de Dados NoSQL com Pymongo

### Objetivo
Implementar um banco de dados NoSQL com MongoDB para fornecer uma visão agregada do modelo relacional. As informações de clientes e contas estão contidas em documentos organizados por cliente.

### Entregáveis
- Conexão ao MongoDB Atlas e criação de um banco de dados.
- Definição de uma coleção `bank` para armazenar documentos de clientes.
- Inserção de documentos com a estrutura mencionada.
- Instruções para recuperação de informações com base em pares de chave-valor.

## Tecnologias Utilizadas
- Python
- SQLite
- SQLAlchemy
- MongoDB
- Pymongo

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.