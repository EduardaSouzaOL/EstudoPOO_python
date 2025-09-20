class Restaurante:
    restaurantes = []
    def __init__(self,nome, categoria,ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo


    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_riomar = Restaurante('Zio Cucina','Italiano', True)

restaurantes = [restaurante_riomar]

print(restaurantes)
print(vars(restaurante_riomar))
