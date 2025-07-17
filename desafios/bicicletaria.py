class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("- Bim bim...")
        
    def parar(self):
        print("-! Parando bicicleta...")
        print("! Bicicleta parada!")
        
    def correr(self):
        print("-- Vhrummmmm...")
        
        

b1 = Bicicleta("Vermelha","Caloi",2022,600)
print("Bicicleta:", b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("azul","monark","2000",189)
b1.buzinar()
b1.correr()
b1.parar()

print("Bicicleta:", b2.cor, b2.modelo, b2.ano, b2.valor)
b2.buzinar()
