carrinho = []
total = 0.0

# Entrada para o usuario digitar quantos produtos deseja comprar
n = int(input("Digite quantos produtos você deseja comprar: ").strip())

# Agora vamos repetir isso n vezes (uma vez pra cada produto)
for _ in range(n):
    # Entrada para o usuario digitar o nome e o preço, exemplo: "Pão 3.50"
    linha = input("Insira o nome e o preço do produto: ").strip() 
    
    # Buscar espaço entre nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Agora separamos o nome do produto e o preço
    item = linha[:posicao_espaco]  # Retorna tudo, omitindo o espaço "Pão"
    preco = float(linha[posicao_espaco + 1:])  # Isso é o preço, tipo 3.50
    
    # Guardamos no carrinho
    carrinho.append((item, preco))
    total += preco  # Somamos o preço no total

# Agora mostramos tudo o que foi comprado
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# E mostramos o total
print(f"Total: R${total:.2f}")