# 1. A CLASSE PAI (Define o "contrato" / a interface comum)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    # Este método é genérico e espera-se que as classes filhas o substituam.
    def fazer_som(self):
        print(f"{self.nome} fez um som genérico.")

# 2. AS CLASSES FILHAS (Implementações específicas)
class Cachorro(Animal):
    # Sobrescrevendo (overriding) o método da classe pai
    def fazer_som(self):
        print(f"{self.nome} latiu: Au, au!")

class Gato(Animal):
    # Sobrescrevendo (overriding) o método da classe pai
    def fazer_som(self):
        print(f"{self.nome} miou: Miau!")

# --- A MÁGICA DO POLIMORFISMO EM AÇÃO ---

# Criando objetos de diferentes classes
animal_generico = Animal("Criatura")
rex = Cachorro("Rex")
frajola = Gato("Frajola")

# Criando uma lista que contém objetos de TIPOS DIFERENTES
animais = [animal_generico, rex, frajola]

print("--- Chamando o mesmo método em todos os objetos ---")
# O loop trata todos da mesma forma: como um 'Animal'.
# Ele não precisa saber se é um Cachorro ou um Gato.
for animal in animais:
    # A chamada é a mesma: animal.fazer_som()
    # Mas o resultado (o comportamento) é diferente para cada um!
    animal.fazer_som()