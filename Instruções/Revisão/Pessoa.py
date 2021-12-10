# Classe
class Pessoa():
  # Atributos
  def __init__(self, nome, idade, cpf, cnh, sexo):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
    self.cnh = cnh
    self.sexo = sexo
  
  # Métodos
  def dizerNome(self):
    print(f'Olá, meu nome é {self.nome}')
  
  def maioriade(self):
    if (self.idade >= 18):
      return print(f'Você tem {self.idade} anos. Você é de maior!')

    return print(f'Você tem {self.idade} anos. Você é de menor!')