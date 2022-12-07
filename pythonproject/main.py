import requests
import json

token = '2300030913159ea7186244d19f1d0ff5'

response_post = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
 "name": "PANKRAT",
 "photo": "https://assets.stickpng.com/images/580b57fcd9996e24bc43c325.png"
})

print(response_post.text)


response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1456,
    "name": "Den_Pankrat",
    "photo": "https://assets.stickpng.com/images/580b57fcd9996e24bc43c325.png"
})

print(response_put.text)

response_pokebol = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1456"
})

print(response_pokebol.text)



# response = requests.get('https://pokemonbattle.me:5000/trainers')
# response_pretty = json.dumps(response.json(), indent=4, ensure_ascii=False)