# Entrada do número de pacientes
n = int(input("Informe o número de pacientes: ").strip())
# Lista para armazenar pacientes
pacientes = []
# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input("Informe o nome, idade e status do paciente: ").strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Ordenação por prioridade: urgente > idosos > demais
def prioridade(paciente):
    nome, idade, status = paciente
    
    # Prioridade 1: Urgente (menor valor = maior prioridade)
    if status == "urgente":
        urgencia = 0
    else:
        urgencia = 1
    
    # Prioridade 2: Para urgentes, ordena por idade (mais velhos primeiro)
    # Para não-urgentes, verifica se é idoso
    if status == "urgente":
        criterio2 = -idade  # Negativo para ordem decrescente de idade
    elif idade >= 60:
        criterio2 = 0  # Idosos não-urgentes
    else:
        criterio2 = 1  # Não-idosos não-urgentes
    
    # Prioridade 3: Ordem de chegada
    ordem_chegada = pacientes.index(paciente)
    
    return (urgencia, criterio2, ordem_chegada)

# Ordena a lista usando a função de prioridade
pacientes_ordenados = sorted(pacientes, key=prioridade)

# Extrai apenas os nomes para a saída
nomes = [paciente[0] for paciente in pacientes_ordenados]

# Exibe a ordem de atendimento
print("Ordem de Atendimento: " + ", ".join(nomes))