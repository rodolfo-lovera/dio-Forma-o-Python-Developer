# Desafio: Integração de Python com APIs

Este repositório contém a resolução de dois desafios de projeto que envolvem a integração de Python com bancos de dados (SQLite e MongoDB) e o desenvolvimento de uma API usando Flask na plataforma COLAB. Os projetos foram desenvolvidos para a formação Python Developer da DIO.me.

## Projeto 1: Integração de Python com SQLite e MongoDB

### Descrição
Esse repositório contém arquivos com a prática de integração do SQLite e MongoDB com Python por meio das bibliotecas SQLAlchemy e Pymongo. Nessas práticas, tabelas e coleções são criadas e consultas básicas são realizadas. Projeto desenvolvido para o desafio de projeto da formação Python Developer da DIO.me.

### Objetivo
Implementar uma aplicação de integração com SQLite com base em um esquema relacional disponibilizado. Utilize o esquema dentro do contexto de cliente e conta para criar as classes de sua API. Essas classes irão representar as tabelas do banco de dados relacional dentro da aplicação.

### Entregáveis
- Definição do esquema do banco de dados usando classes do SQLAlchemy.
- Inserção de um conjunto de dados mínimo para manipulação das informações.
- Execução de métodos de recuperação de dados via SQLAlchemy.
- Conexão ao MongoDB Atlas e criação de um banco de dados.
- Definição de uma coleção `bank` para armazenar documentos de clientes.
- Inserção de documentos com a estrutura mencionada.
- Instruções para recuperação de informações com base em pares de chave-valor.

## Projeto 2: Desenvolvimento de uma API com Flask no COLAB

### Descrição
Esse projeto envolve a entrega de uma API desenvolvida no framework Flask utilizando a Plataforma COLAB. O objetivo principal está relacionado com a leitura de uma planilha de dados no formato JSON utilizando uma API no ambiente de desenvolvimento colaborativo COLAB. Projeto desenvolvido para o desafio de projeto da formação Python Developer da DIO.me.

### Objetivo
Para este projeto, o desafio final envolve a entrega de uma API desenvolvida no framework Flask utilizando a Plataforma COLAB. O objetivo principal está relacionado com a leitura de uma planilha de dados no formato JSON utilizando uma API no ambiente de desenvolvimento colaborativo COLAB. Nosso servidor Flask deve trazer a planilha gerada em JSON, assim como apresentar um “Hello World” neste exemplo. Para isso, deve ser dado um `{Public_URL}/index` no navegador para chegar ao nosso endpoint, pois criamos apenas uma rota, ou seja, `/index`.

### Entregáveis
- Desenvolvimento de uma API usando Flask.
- Leitura de uma planilha de dados no formato JSON.
- Implementação de um endpoint `/index` para retornar os dados e uma mensagem "Hello World".

## Tecnologias Utilizadas
- Python
- SQLite
- SQLAlchemy
- MongoDB
- Pymongo
- Flask
- COLAB

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.