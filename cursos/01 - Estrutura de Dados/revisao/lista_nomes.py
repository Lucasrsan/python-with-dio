lista_de_nomes = []

print("Digite os nomes que deseja e se quiser finalizar digite 'fim'.")

while True:
    nome = input("Nome: ").strip()
    
    if nome.lower() == 'fim':
        break
    if nome:
        lista_de_nomes.append(nome.capitalize())
        
print(lista_de_nomes)