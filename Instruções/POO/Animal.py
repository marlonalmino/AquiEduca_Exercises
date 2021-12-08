# Classe
class Animal:
  def __init__(self, nome, raca, porte):
    # Atributos
    self.nome = nome
    self.raca = raca
    self.porte = porte

  # Método da Classe Mãe
  def patas(self):
    print('Tem 6 patas\n')

# Instância de Animal
animal = Animal('Nick', 'Pinscher-Poodle', 'P')
print(f'Nome: {animal.nome} \nRaça: {animal.raca} \nPorte: {animal.porte}')
animal.patas()

# Classe Herdada
class Cachorro(Animal):
  def __init__(self, nome, raca, porte):
    # Atributos Herdados
    super().__init__(nome, raca, porte)

  # Método substituído (polimorfismo)
  def patas(self):
    print('Tem 4 patas \n')

# Instância de Cachorro
cachorro = Cachorro('Thor', 'Rottvailer', 'G')
print(f'Nome: {cachorro.nome} \nRaça: {cachorro.raca} \nPorte: {cachorro.porte}')
cachorro.patas()

# Classe Herdada
class Gato(Animal):
  def __init__(self, nome, raca, porte, pelagem):
    # Atributo exclusivo de Gato
    self.pelagem = pelagem

    # Atributos herdados
    super().__init__(nome, raca, porte)

# Instância de Gato
gato = Gato('Senhorita', 'Grega', 'P', 'Curta')
print(f'Nome: {gato.nome} \nRaça: {gato.raca} \nPorte: {gato.porte} \nPelagem: {gato.pelagem}')

# Método patas() herdado de Animal
gato.patas()