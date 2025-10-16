import requests

class RickAndMortyAPI:
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api"

    def get_character(self, id):
        """
        Obtiene los datos de un personaje específico por su ID.

        Parametro:
            id (int): El ID del personaje que se quiere obtener.

        Returns:
            dict: Un diccionario con los datos del personaje si la petición es exitosa.
            None: Si ocurre un error en la petición.
        """
        
        # Construimos la URL completa para el endpoint del personaje
        url = f"{self.url}/character/{id}"
        
        try:
            # Hacemos la petición GET a la URL
            res = requests.get(url)
            
            # Verificamos si la petición fue exitosa (código de estado 200)
            res.raise_for_status()
            
            # Convertimos la respuesta a formato JSON (un diccionario de Python)
            return res.json()

        except requests.exceptions.RequestException as e:
            # Capturamos posibles errores de conexión o HTTP
            print(f"Ocurrió un error al hacer la petición: {e}")
            return None
