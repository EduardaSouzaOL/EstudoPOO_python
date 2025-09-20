#EXERCICIO 2

# Implemente uma classe chamada Carro com os atributos básicos,
# como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []
    def __init__(self,modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo}, {carro.cor}, {carro.ano}')



carro_duda = Carro('Porsche','Preto', '2030')

print(vars(carro_duda))


# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
# Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria,ativo, classificacao, melhorprato):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.classificacao = classificacao
        self.melhorprato = melhorprato
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome}, {restaurante.categoria}, | {restaurante.ativo} |' )
            print(f'{restaurante.classificacao} | {restaurante.melhorprato}')


class Restaurante:
    def __init__(self, nome,categoria, capacidade,nota_avaliacao,ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'{self.nome} | {self.categoria}'



class Cliente:
    def __init__(self, nomeCliente, endereco, pratofavorito, idade = 0):
        self.nomeCliente = nomeCliente
        self.endereco = endereco
        self.pratofavorito = pratofavorito
        self.idade = idade

restaurante_Outback = Restaurante('Outback','Fast Food', '5', True)


Cliente1 = Cliente('Duda','recife','ribs on barbie',20)
Cliente2 = Cliente('João','recife','chicken',22)
Cliente3 = Cliente('Tina','recife','mac n cheese',13)










