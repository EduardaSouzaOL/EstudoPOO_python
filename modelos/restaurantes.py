
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
# instanciando objeto

# variavel tipo restaurante, usar classe(criar objeto na memoria)
restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

#criar uma lista
restaurantes = [restaurante_praca,
restaurante_praca]
#visualizar lista, o local da memoria onde ta armazenado 
print(restaurantes)
# atribua o valor Italiana ao atributo cateoria da instancia trdyaurante_praca da cllasse Restaurante
restaurante_praca.categoria = 'Italiana'
restaurante_praca.nome = 'Zio cucina'
# acesse o valor do atributo nome da instancia rstaurante_praaca da cçasse Restaurante
nome_restaurante = restaurante_praca.nome

if restaurante_praca.ativo:
    print('o restauranteestá ativo')
else:
    print('O restaurate está inativo')
#valor do atributo de classe categoria diretamente da classe Restaurante
categoria = Restaurante.categoria
print(categoria)
restaurante_praca.nome = 'Bistrô'
restaurante_pizza = Restaurante()
restaurante_pizza.categoria = 'Fast food' 
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.ativo = True

if restaurante_pizza == 'Fast Food':
    print('A catgria é Fast Food')
else:
    ('A categoria não é Fast Food')

print(f"'Nome: {restaurante_praca.nome},\n Categoria: {restaurante_praca.categoria}")