idade = int(input("Insira a sua idade: "))
if idade >= 18:
    print("Você é maior de idade, apto para tirada da CNH.")
elif idade >= 13:
    print("Faltam ainda " + str(18-idade) + " anos para você poder tirar sua CNH.")
else: 
    print("Você é uma criança e já está querendo tirar a CNH, faltam " + str(18-idade) + " anos para você poder tirar a CNH.")