import requests
import pandas as pd
import random

# Lista onde irão conter os dados dos Pokémons
lista = []

while True:
    poke_answer = input('Deseja adicionar algum Pokémon a lista?(S/N)')

    if poke_answer.lower() == 's':
        numero = random.randint(1,1000)
        url = f"https://pokeapi.co/api/v2/pokemon-form/{numero}"
        response = requests.get(url)
        
        # Tranformando os dados que foram pegos com requests e tranformando-os de .json para um dicionário Python
        data = response.json()

        # Adicionado os dados pegos no dicionário numa lista de dicionários
        lista.append({
            'id': data['id'],
            'nome': data['name']
        })
        for i in lista:
            print(f'Nome: {i["nome"]}')
            print(f'Id: {i["id"]}\n')
    elif poke_answer.lower() == 'n':
        print('Iremos gerar uma lista dos Pokémons que você encontrou!')
        print()

        # Transformando a lista em um DataFrame
        df = pd.DataFrame(lista)
        # Tranformando o DataFrame em csv
        df.to_csv('pokelista.csv', index=False)

        print('Lista gerada com sucesso!')
        print()
        print('Obrigado por consultar a Pokélista!')
        break
    else:
        print('Algo deu errado. Tente novamente.')
        continue
    
        





