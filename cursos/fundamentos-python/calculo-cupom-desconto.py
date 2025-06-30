descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

preco = float(input().strip())
cupom = input().strip()

if cupom in descontos:
    preco -= preco * descontos[cupom]
    print(f"{preco:.2f}")
else:
    print("Por favor insira um cupom existente!")