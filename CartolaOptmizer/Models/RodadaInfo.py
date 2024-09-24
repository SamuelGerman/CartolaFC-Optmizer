class RodadaInfo:
    def __init__(self,num_rodada, partidas_validas):
        self.num_rodada = num_rodada
        self.partidas_validas = partidas_validas # lista com as partidas validas da rodada
        #quais outras informações relevantes para rodada? talvez uma lista de 'confrontos etiquetados ou manjados, por exemplo, lider contra lanterna
        #melhor ataque x melhor defesa, melhor mandante x pior visitante, melhor visitante x pior mandante.