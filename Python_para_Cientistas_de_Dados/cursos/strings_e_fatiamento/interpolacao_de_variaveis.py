pi = 3.14159

nome = 'Gary'
idade = 27
profissao = 'trader'
linguagem = 'street'

# old style %

print ('\nMe chamo %s. Tenho %d anos. Trabalho com %s e uso a linguagem da %s.' % (nome, idade, profissao, linguagem))

# %s = str
# %d = int
# %f = float


# metodo format

print('Me chamo {}. Tenho {} anos, trabalho como {} e uso a linguagem da {}.'.format(nome, idade, profissao, linguagem))

print('Me chamo {3}. Tenho {2} anos, trabalho como {0} e uso a linguagem da {1}.'.format(nome, idade, profissao, linguagem))

print('Me chamo {name}. Tenho {age} anos, trabalho como {profession} e uso a linguagem da {language}.'.format(name=nome, age=idade, profession=profissao, language=linguagem))

gary = {'nome': 'Gary', 'idade': 27, 'profissao': 'trader', 'linguagem': 'rua'}

print('Me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e uso a linguagem da {linguagem}.'.format(**gary))

# metodo f string

print(f'Me chamo {nome}, tenho {idade}, trabalho como {profissao} e uso a linguagem da {linguagem}.')

print(f'Valor de Pi = {pi:.2f}')

print(f'Valor de Pi = {pi:10.2f}')