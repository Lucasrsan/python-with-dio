# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input("Insira o numero de participantes: ").strip())

# Loop para armazenar participantes e seus temas
for _ in range(n):
    linha = input("Insira o nome e o tema escolhido: ").strip()
    nome, tema = linha.split(",")

    tema = tema.strip().title()  # Aqui transforma o tema em maiúsculo

    # Se o tema ainda não está no dicionário, criamos uma lista nova
    if tema not in eventos:
        eventos[tema] = []
    
    # Adicionamos o nome da pessoa na lista do tema
    eventos[tema].append(nome.strip())

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
