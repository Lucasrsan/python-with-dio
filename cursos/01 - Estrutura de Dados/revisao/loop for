# entrada de senha do usuário
senha = input("Insira a sua senha: ")
tem_letra_maiuscula = False
tem_numero = False
tem_comprimento_ok = False

# checklist de requisitos de senha
for caractere in senha:
    if caractere.isupper():
        tem_letra_maiuscula = True
    elif caractere.isdigit():
        tem_numero = True

if len(senha) >=  8:
        tem_comprimento_ok = True
        
if tem_letra_maiuscula and tem_numero and tem_comprimento_ok:
    print("Senha válida!")
else:
    if not tem_letra_maiuscula:
        print("- Necessário no mínimo 1 letra maiúscula")
    if not tem_numero:
        print("- Necessário no mínimo um número")
    if not tem_comprimento_ok:
        print("- Necessário no mínimo 8 caracteres")