def coletar_notas(): # cria a função que retorna as notas
    notas_coletadas = [] # cria a lista vazia
    print("--- Entrada de Notas ----")
    print("Digite as notas dos alunos. Digite 'fim' para terminar.") # orientação inicial
    
    while True:
        entrada = input("Nota: ").strip() # recebe entrada do usuário tanto numero como string e remove espaços
        if entrada.lower() == 'fim': # verifica a condição de saida
            print("Entrada de notas finalizada.")
            break # quebra o loop
        try:
            nota = float(entrada) # transforma o numero em formato string para float
            notas_coletadas.append(nota) # adiciona a nota númerica na lista
        
        except ValueError:
            print("Entrada Invalida! Por favor, digite um número ou 'fim'.") # orientação
    
    return notas_coletadas # retorna a lista das notas coletadas preenchida com os números
    
def analisar_turma(nota_dos_alunos): # cria uma função que recebe um parâmetro que receberá a lista de notas coletadas
    if nota_dos_alunos: # verifica se a lista não está vazia
        media = sum(nota_dos_alunos) / len(nota_dos_alunos) # calcula a media das notas
        maior_nota = nota_dos_alunos[0] # valor inicial indice 0
        menor_nota = nota_dos_alunos[0] # valor inicial indice 0
        
        for nota_atual in nota_dos_alunos: # inicia o loop para percorrer cada nota na lista e comparar
            if nota_atual > maior_nota:
                maior_nota = nota_atual
            if nota_atual < menor_nota:
                menor_nota = nota_atual
        
        print("\n--- Analise de Notas ---")
        print(f"Nota dos Alunos: {nota_dos_alunos}")
        print(f"Maior Nota: {maior_nota:.2f}")
        print(f"Menor Nota: {menor_nota:.2f}")
        print(f"Media dos Alunos: {media:.2f}")

#nota_dos_alunos = coletar_notas()
#analisar_turma(nota_dos_alunos)
    
if __name__ == '__main__':
    nota_dos_alunos = coletar_notas()
    analisar_turma(nota_dos_alunos)
