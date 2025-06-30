#Criando o dicionário descontos
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

#Lê valor em formato decimal e remove espaços
preco = float(input().strip())
cupom = input().strip()
#Verifica se o cupom está no dicionario
if cupom in descontos:
    preco -= preco * descontos[cupom]
    print(f"{preco:.2f}")
    
else:
    print("Por favor insira um cupom existente!")