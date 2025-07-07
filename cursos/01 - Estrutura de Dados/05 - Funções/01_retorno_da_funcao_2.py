def media_aluno(nota1, nota2, nota3):
    """Calcula a média de um aluno com três notas."""
    media = (nota1 + nota2 + nota3) / 3
    return media  # Devolve a média calculada

nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
nota3 = float(input("Insira a terceira nota do aluno: "))
    


# Chamamos a função e guardamos o valor retornado em uma variável
media_aluno_calculada = media_aluno(nota1,nota2,nota3)
print(f"A média do aluno é {media_aluno_calculada}")