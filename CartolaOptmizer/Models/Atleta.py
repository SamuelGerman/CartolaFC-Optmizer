class Atleta:
    def __init__(self, scout, jogos_num, atleta_id, rodada_id, clube_id, posicao_id, status_id, 
                 pontos_num, media_num, variacao_num, preco_num, entrou_em_campo, slug, apelido, nome, foto):
        self.scout = scout  # Dicionário com os scouts do jogador (ex: CA, DE, FS)
        self.jogos_num = jogos_num
        self.atleta_id = atleta_id
        self.rodada_id = rodada_id
        self.clube_id = clube_id
        self.posicao_id = posicao_id
        self.status_id = status_id
        self.pontos_num = pontos_num
        self.media_num = media_num
        self.variacao_num = variacao_num
        self.preco_num = preco_num
        self.entrou_em_campo = entrou_em_campo
        self.slug = slug
        self.apelido = apelido
        self.nome = nome
        self.foto = foto  # URL da foto do jogador

    def __str__(self):
        return f"Atleta {self.apelido} (ID: {self.atleta_id}, Clube: {self.clube_id})"
