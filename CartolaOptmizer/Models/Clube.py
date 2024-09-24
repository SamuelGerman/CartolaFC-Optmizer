class Clube:
    def __init__(self, id, nome, abreviacao, slug, apelido, nome_fantasia, escudos, url_editoria):
        self.id = id
        self.nome = nome
        self.abreviacao = abreviacao
        self.slug = slug
        self.apelido = apelido
        self.nome_fantasia = nome_fantasia
        self.escudos = escudos  # Espera-se que seja um dicionário com diferentes tamanhos de imagem
        self.url_editoria = url_editoria
        #rivais? outros atributos?

    def __str__(self):
        return f"Clube {self.nome} (ID: {self.id}) - Apelido: {self.apelido}"
