# Importações
from Pessoa import Pessoa
from Medico import Medico

# Capturando dados para Pessoa
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cpf = input('Digite seu CPF: ')
sexo = input('Digite seu sexo: ')

# Instanciando Pessoa
pessoa = Pessoa(nome, idade, cpf, True, sexo)
print(pessoa.__dict__)

# Chamando Métodos de Pessoa
pessoa.dizerNome()
pessoa.maioriade()


# Instanciando Medico
medico = Medico('Gabriela', 27, 'xxxxxxxxxxx', False, 
'Feminino', '489204', 'ginecologista')
print(medico.__dict__)

# Chamando Métodos de Medico
medico.dizerNome()
medico.dizerEspecialidade()