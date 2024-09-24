class Status:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"Status {self.nome} (ID: {self.id})"
