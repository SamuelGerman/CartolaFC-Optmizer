class Partida:
    def __init__(self, visitante, mandante, aproveitamento_visitante, aproveitamento_mandante, 
                 placar_visitante, placar_mandante, clube_visitante_posicao, clube_mandante_posicao, 
                 partida_id, clube_visitante_id, clube_mandante_id, local, partida_data, valida, diferenca_pos):
        self.visitante = visitante
        self.mandante = mandante
        self.aproveitamento_visitante = aproveitamento_visitante  # Lista com sequência de resultados (ex: ['v', 'd', 'e'])
        self.aproveitamento_mandante = aproveitamento_mandante
        self.placar_visitante = placar_visitante
        self.placar_mandante = placar_mandante
        self.clube_visitante_posicao = clube_visitante_posicao
        self.clube_mandante_posicao = clube_mandante_posicao
        self.partida_id = partida_id
        self.clube_visitante_id = clube_visitante_id
        self.clube_mandante_id = clube_mandante_id
        self.local = local
        self.partida_data = partida_data
        self.valida = valida
        self.diferenca_pos = clube_mandante_posicao - clube_visitante_posicao

    def __str__(self):
        return f"Partida {self.visitante} vs {self.mandante} no {self.local} - Data: {self.partida_data}"
