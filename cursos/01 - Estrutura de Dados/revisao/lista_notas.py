lista_notas = []
soma_notas = 0

print("Digite a nota dos alunos e 'fim' para finalizar.")

while True:
    entrada = input("Nota: ").strip()
    if entrada.lower() == 'fim':
        print("Entradas finalizadas.")
        break # quebra o loop
    
    try:
        nota = float(entrada)
        lista_notas.append(nota)
        soma_notas += nota
        
    except ValueError:
        print("Entrada inválida. Por favor digite uma nota ou 'fim' para sair.")
        
        
if lista_notas:
    media_notas = soma_notas / len(lista_notas) 
    maior_nota = lista_notas[0]
    menor_nota = lista_notas[0]
    for nota_atual in lista_notas:
        if nota_atual > maior_nota:
             maior_nota = nota_atual
        elif nota_atual < menor_nota:
             menor_nota = nota_atual
            
    # Impressão dos resultados
    print("\n--- Resultados da Turma ---")
    print(f"Notas inseridas: {lista_notas}")
    print(f"Maior nota: {maior_nota:.2f}")
    print(f"Menor nota: {menor_nota:.2f}")
    print(f"Média das notas: {media_notas:.2f}")

else: # O que acontece se a lista estiver vazia
    print("\nNenhuma nota foi inserida para análise.")