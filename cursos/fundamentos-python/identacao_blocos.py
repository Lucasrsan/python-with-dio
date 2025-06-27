def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro no caixa eletronico.")

    print("Obrigado por ser o nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)