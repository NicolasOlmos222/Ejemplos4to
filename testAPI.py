from config import *

api = RickAndMortyAPI()

data = api.get_character(6)

if data:
    print("¡Datos del personaje obtenidos con éxito!")
    
    print(f"ID: {data.get('id')}")
    print(f"Nombre: {data.get('name')}")
    print(f"Estado: {data.get('status')}")
    print(f"Especie: {data.get('species')}")
    print(f"Imagen: {data.get('image')}")