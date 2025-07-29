lista_de_compras = ["Maça","Banana","Maça","Laranja","Banana","Uva","Maça"]
contagem_itens = {}

for fruta in lista_de_compras:
    if fruta in contagem_itens: #verificar se a chave fruta já existe em nosso dicionario
        contagem_itens[fruta] +=1 # caso exista apenas some ao valor atual
    else:
        contagem_itens[fruta] = 1 #caso não exista, cria chave e defina o valor inicial 1

print("--- Resumo de compra ---")

for item, quantidade in contagem_itens.items(): #converte o dicionario em uma coleção de (chave, valor)
    print(f"{item}: {quantidade}")