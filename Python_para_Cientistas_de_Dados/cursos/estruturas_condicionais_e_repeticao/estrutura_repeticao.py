# estrutura for

texto = input('Informe um texto: ')
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end = ' ')

# estrutura for+else

print() # adiciona quebra de linha

texto = input('Informe um texto: ')
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end = ' ')
else:
    print()
    print('estrutura fora do laço')

print() # adiciona quebra de linha

# estrutura range

list(range(4))

for numero in range(0, 11):
    print(numero, end = ' ')

print()    

for numero in range(0, 51, 5):
    print(numero, end = ' ')

# estrutura while

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n'))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
else:
    print('Obrigado e até a próxima!')

# estrutura break

while True:
    numero = int(input('Informe um número: '))

    if numero == 10:
        break
    
    print(numero)


# estrutura continue

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end = ' ')