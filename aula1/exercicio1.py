# Exercicio para melhorar a classe Musica criada anteriormente


class Musica:
    def __init__(self,nome, artista, duracao = 0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao



musica1 = Musica( nome = 'So tu es', artista= 'Morada', duracao= 200)
musica2 = Musica(nome= 'A casa É Sua' artista= 'Morada', duracao= 200)