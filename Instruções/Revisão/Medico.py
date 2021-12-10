# Importações
from Pessoa import Pessoa

# Classe - Herança
class Medico(Pessoa):
  def __init__(self, nome, idade, cpf, cnh, sexo, crm, especialidade):
    # Atributo Exclusivo do Medico
    self.crm = crm
    self.especialidade = especialidade

    # Atributos Genéricos de Pessoa
    super().__init__(nome, idade, cpf, cnh, sexo)

  # Métodos
    # Polimorfismo
  def dizerNome(self):
    print(f'Boa noite, meu nome é {self.nome}')
  
  def dizerEspecialidade(self):
    print(f'Eu sou {self.especialidade}!')