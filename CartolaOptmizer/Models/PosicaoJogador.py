class Posicao:
    def __init__(self, id, nome, abreviacao):
        self.id = id
        self.nome = nome
        self.abreviacao = abreviacao

    def __str__(self):
        return f"Posição {self.nome} (Abreviação: {self.abreviacao})"
