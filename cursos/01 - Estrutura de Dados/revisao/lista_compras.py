lista_de_compras = [] # Cria uma lista vazia
print("Digite os itens da sua compra, um por um. Digite 'fim' para terminar.") # exibi a orientação para usuario

while True:
    item = input("Item: ").strip() # Recebe os itens de entrada do usuario e remove os espaços extras

    if item.lower() == 'fim': # Verifica a condição de parada
        break # Sai do loop

    if item: 
        lista_de_compras.append(item.capitalize()) # adiciona o item a lista e formata o texto
    
contagem_itens = {} # Cria um dicionario vazio
for fruta in lista_de_compras:
    if fruta in contagem_itens: # Verificar se a chave fruta já existe em nosso dicionario
        contagem_itens[fruta] +=1 # Caso exista apenas some ao valor atual
    else:
        contagem_itens[fruta] = 1 # Caso não exista, cria chave e defina o valor inicial 1

print("--- Resumo de compra ---")

for item, quantidade in contagem_itens.items(): # Converte o dicionario em uma coleção de (chave, valor)
    print(f"{item}: {quantidade}")