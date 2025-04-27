# Pokélista 🎮✨
Um pequeno projeto em Python para montar uma lista aleatória de Pokémons usando a PokeAPI!
Ideal para treinar conceitos de requisições HTTP, tratamento de dados JSON, manipulação de listas e uso de DataFrame com Pandas.

## 📜 Descrição
O programa:

Pergunta ao usuário se ele quer adicionar um Pokémon à lista (S para sim, N para não).

Quando o usuário responde S, ele sorteia um Pokémon aleatório entre os primeiros 1000 e puxa seus dados da API.

Os dados (id e nome) são armazenados em uma lista de dicionários.

Quando o usuário responde N, o programa gera um arquivo pokelista.csv com todos os Pokémons encontrados.

## 🚀 Tecnologias usadas
* Python 3

* Requests

* Pandas

### ⚙️ Como executar o projeto

1- Clone o repositório:

<pre>git clone https://github.com/seu-usuario/pokelista.git
cd pokelista</pre>


2 - Instale as dependências necessárias:

<pre>pip install requests pandas</pre>

3 - Rode o script:

<pre>python pokelista.py</pre>

4 - Siga as instruções no terminal!


## 🛠️ Funcionalidades
* Consulta de Pokémon de forma aleatória.

* Salvamento dos dados em um arquivo .csv.

* Tratamento básico de erros em requisições.

* Validação de entrada do usuário.


## ❗ Observação
* Nem todos os números entre 1 e 1000 correspondem a Pokémons válidos na PokeAPI. Caso aconteça erro na requisição, o programa pedirá para tentar novamente.

* Apenas o id e o nome do Pokémon são armazenados, mas o projeto pode ser facilmente expandido para salvar outros dados (tipo, habilidades, etc).


## 📚 Melhorias futuras
* Permitir que o usuário escolha um intervalo de IDs.

* Salvar mais informações sobre os Pokémons.

* Melhorar o tratamento de erros de conexão.

* Adicionar uma interface gráfica simples (GUI).


### Autor: Victor Kakiuti Boer


## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

