# cria uma função sacar
def sacar(valor, saldo):
    if saldo >= valor:
        saldo -= valor
        print("\n--------------------------------")
        print(f"\nValor de R${valor:.2f} sacado.")
        print(f"\nSaldo atual: R${saldo:.2f}.")
        print("\n--------------------------------")
        return saldo
    else:
        print("\n--------------------------------")
        print("\nSaldo insuficiente")
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("\n--------------------------------")
        return saldo

# cria uma função de depositar
def depositar(valor, saldo):
    if valor > 0:
        saldo += valor
        print("\n--------------------------------")
        print(f"\nForam depositados R${valor:.2f}.")
        print(f"\nSaldo atual: R${saldo:.2f}.")
        print("\n--------------------------------")
        return saldo
    else:
        print("O valor é inválido")
        return saldo
 
 # define um saldo inicial
saldo = 500
 
 # cria a função menu de opções
def mostrar_menu():
     print("\n=== CAIXA ELETRÔNICO ===")
     print("s - Sacar")
     print("d - Depositar")
     print("c - Consultar Saldo")
     print("q - Sair")
     print("============================")

while True: 
    mostrar_menu() # exibir menu de opções 
    opção = input("Escolha uma das opções: ")
    if opção == 's':
         valor = float(input("Digite o quanto deseja sacar: R$  "))
         saldo = sacar(valor,saldo)
    elif opção == 'd':
        valor = float(input("Digite o valor que deseja depositar: R$ "))
        saldo = depositar(valor,saldo)
    elif opção == 'c':
        print("\n--------------------------------")
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("\n--------------------------------")
    elif opção == 'q':
        print("Obrigado por ser o nosso cliente.\nTenha um bom dia!:)")
        break
    else:
        print("Opção inválida! Tente novamente.")