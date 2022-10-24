# AND = para ser True, tudo precisa que ser True
print(True and True)
print(True and False)
print(False and False)

# OR = para ser True, apenas um precisa ser True
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 200
limite = 100
conta_especial = True

contatos_emergencia = []

# operador and
saldo >= saque and saque <= limite

# operador or
saldo >= saque or saque <= limite

# operador not
not 1000 > 1500

not contatos_emergencia

not 'saque 1500;'

not ''

# operador parênteses: utilizado  como boa prática para facilitar a leitura do código
saldo>= saque and saque <=limite or conta_especial and saldo >= saque

(saldo>= saque and saque <=limite) or (conta_especial and saldo >= saque)