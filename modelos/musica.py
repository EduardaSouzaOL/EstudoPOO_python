#pratica aula 01
class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Dispiei'
musica1.artista = 'BK'
musica1.duracao = 310

musica2 = Musica()
musica2.nome = '20 ligações'
musica2.artista = 'Baco'
musica2.duracao = 320

musica3 = Musica()
musica3.nome = 'SOLTO'
musica3.artista = 'DJONGA'
musica3.duracao = 330

print(f'Música: {musica1.nome} - Artista: {musica1.artista} - {musica1.duracao} segundos')

