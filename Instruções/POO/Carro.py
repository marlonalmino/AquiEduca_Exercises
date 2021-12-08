class Veiculo:
  def __init__(self, marca, ano, cor):
    self.marca = marca
    self.ano = ano
    self.cor = cor

carro = Veiculo('Fiat', 2014, 'Vermelho')
# carro2 = Carro('GM', 2018, 'Prata')

# print(f'Marca: {carro.marca} \nAno: {carro.ano} \nCor: {carro.cor}')
# print(f'Marca: {carro2.marca} \nAno: {carro2.ano} \nCor: {carro2.cor}')

class Carro(Veiculo):
  def __init__(self, marca, ano, cor, rodas):
    self.rodas = rodas
    
    super().__init__(marca, ano, cor)

carro = Carro('Ford', 2016, 'Preto', 'Picapi')
print(carro.marca)
print(carro.ano)
print(carro.cor)
print(carro.rodas)


class Moto(Veiculo):
  def __init__(self, marca, ano, cor, potencia):
    self.potencia = potencia

    super().__init__(marca, ano, cor)

moto = Moto('Honda', 2018, 'Vermelho', 250)
print(moto.marca)
print(moto.ano)
print(moto.cor)
print(moto.potencia)
# Alt + Shift + baixo