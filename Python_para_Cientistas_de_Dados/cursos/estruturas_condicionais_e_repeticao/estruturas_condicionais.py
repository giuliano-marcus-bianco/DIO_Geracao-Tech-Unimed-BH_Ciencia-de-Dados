maior_idade = 18
emancipado = 15

idade = int(input('informe a sua idade: '))

# estrutura if_if

if idade >= maior_idade:
    print('Maior de idade.')

if idade < maior_idade:
    print('Menor de idade.')

# estrutura if_else

if idade >= maior_idade:
    print('Maior de idade.')

else:
    print('Menor de idade.')

# estrutura if_elif

if idade >= maior_idade:
    print('Maior de idade.')

elif idade >= emancipado:
    print('Menor de idade mas emancipado.')

else:
    print('Menor de idade.')

# estrutura aninhada

conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso.')
    if saque <= (saldo + cheque_especial):
        print('Saque realizado com uso de cheque especial.')
    else:
        print('Não foi possível realizar o saque.')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso.')
    else:
        print('Saldo insuficiente.')
else:
    print('Sistema não reconheceu o seu tipo de conta. Entre em contato com o seu gerente.')

# estrutura if ternário

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')