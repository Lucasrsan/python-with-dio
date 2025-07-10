#Criando um dicionario de descontos []
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "DESCONTO50": 0.50,
    "SEM_DESCONTO": 0.00
}

#Lê valor em formato decimal e remove espaços .strip()
preco = float(input("Insira o preço: ").strip())
cupom = input("Insira o cupom: ").strip()
#Verifica se o cupom está no dicionario por meio do 'in'
if cupom in descontos:
    preco -= preco * descontos[cupom]
    print(f"O valor total ficará: {preco:.2f}") 
else:
    print("Por favor, insira um cupom válido!")
