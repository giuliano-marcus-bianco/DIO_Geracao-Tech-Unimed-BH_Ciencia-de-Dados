def sacar(valor):
    saldo = 1000
    if saldo >= valor:
        print('valor sacado!')
        print('retire seu dinheiro no caixa!')
        saldo -= valor
        print(f'seu novo saldo é de {saldo}')
    
    else:
        print('seu saldo não é suficiente')

def depositar( valor):
    saldo = 1000
    saldo += valor
    print(saldo)


depositar(1000)

sacar(500)