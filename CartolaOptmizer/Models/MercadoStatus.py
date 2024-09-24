class MercadoStatus:
    def __init__(self, rodada_atual, status_mercado, temporada, fechamento):
        self.rodada_atual = rodada_atual
        self.status_mercado = status_mercado
        self.temporada = temporada
        self.fechamento = fechamento  # Fechamento deve ser um dicionário com informações de data

    def __str__(self):
        return f"Mercado Status - Rodada Atual: {self.rodada_atual}, Temporada: {self.temporada}"
