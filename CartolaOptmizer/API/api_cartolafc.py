import requests
from cartola_endpoint import CartolaEndpoint

class CartolaAPI:
    BASE_URL = 'https://api.cartolafc.globo.com'  # URL base da API

    def __init__(self):
        self.endpoints = []
        self.initialize_endpoints()

    def initialize_endpoints(self):
        # Inicializa a lista de endpoints
        self.endpoints.append(CartolaEndpoint("Mercado Status", "mercado/status"))
        self.endpoints.append(CartolaEndpoint("Proximas Partidas", "partidas"))
        self.endpoints.append(CartolaEndpoint("Partidas rodada especifica", "partidas/{}"))  # Placeholder para rodada
        self.endpoints.append(CartolaEndpoint("Clubes", "clubes"))
        self.endpoints.append(CartolaEndpoint("Atletas do mercado", "atletas/mercado"))

    def get(self, endpoint_name, params=None):
        """Método generalizado para obter dados de um endpoint específico"""
        endpoint = next((ep for ep in self.endpoints if ep.nickname == endpoint_name), None)
        if not endpoint:
            print(f"Endpoint '{endpoint_name}' não encontrado.")
            return None

        url = f"{self.BASE_URL}/{endpoint.endpoint.format(params) if params else endpoint.endpoint}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()  # Retorna a resposta JSON
        else:
            print(f"Erro ao buscar dados do endpoint '{endpoint_name}': {response.status_code}")
            return None

if __name__ == "__main__":
    api = CartolaAPI()
    jogadores = api.get("Atletas do mercado")
    clubes = api.get("Clubes")
    partidas = api.get("Proximas Partidas")
    partidas_rodada = api.get("Partidas rodada especifica", params=1)  # Exemplo de chamada com rodada
    mercado_status = api.get("Mercado Status")
  