	# Definición
class Animal:
  def __init__(self, especie):
    self.especie = especie
  def mostrar(self):
    print(f"Especie: {self.especie}")
class Mamifero(Animal):
  def __init__(self, especie, tipo):
    super().__init__(especie) # Constructor Padre
    self.tipo = tipo
  def amamantar(self):
    print(f"{self.especie} amamanta 🍼 a crías")
  def mostrar(self):
    super().mostrar() # Llamada al método del padre
    print(f"Tipo: {self.tipo} (mamífero)")
    self.amamantar()
 
class Ave(Animal):
  def __init__(self, especie, volar):
    super().__init__(especie) # Constructor Padre
    self.volar = volar
  def poner_huevo(self):
    print(f"{self.especie} pone huevos 🥚")
  def mostrar(self):
    super().mostrar() # Llamada al método del padre
    print(f"Puede volar: {self.volar} (ave)")
    self.poner_huevo()
 
class Reptil(Animal):
  def __init__(self, especie, tipo, venenoso):
    super().__init__(especie) # Constructor Padre
    self.tipo = tipo
    self.venenoso = venenoso
  def reptar(self):
    print(f"{self.especie} se arrastra 🐍")
  def mostrar(self):
    super().mostrar() # Llamada al método del padre
    print(f"Tipo: {self.tipo} - Venenoso: {self.venenoso} (reptil)")
    self.reptar()
# Uso
caballo = Mamifero("Caballo", "Terrestre")
caballo.mostrar()
paloma = Ave("Paloma", True)
paloma.mostrar()
coco = Reptil("Cocodrilo", "Acuático", False)
coco.mostrar()
# Uso isinstance()
caballo_es_mamifero = isinstance(caballo, Mamifero)
print("Caballo Es Mamifero: ", caballo_es_mamifero)
caballo_es_animal = isinstance(caballo, Animal)
print("Caballo Es Animal: ", caballo_es_animal)
caballo_es_ave = isinstance(caballo, Ave)
print("Caballo Es Ave: ", caballo_es_ave)
# Uso issubclass()
mamifero_es_animal = issubclass(Mamifero, Animal)
print("Mamifero Es Animal: ", mamifero_es_animal)
mamifero_es_ave = issubclass(Mamifero, Ave)
print("Mamifero Es Ave: ", mamifero_es_ave)