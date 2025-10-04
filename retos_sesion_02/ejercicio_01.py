class Animal:
  origen = "feral"
  def __init__(self, especie, tipo, lugar):
    self.especie = especie
    self.tipo = tipo
    self.lugar = lugar
    
print("---Animales encontrados---")

mamifero1 = Animal("Tigre", "mamifero", "selva")
mamifero2 = Animal("Elefante", "mamifero", "sabana")

reptil = Animal("Cocodrilo", "reptil", "pantano")

ave = Animal("Aguila", "ave", "montaña")

print("Animal 1:", mamifero1.origen, mamifero1.especie, mamifero1.tipo, mamifero1.lugar)
print("Animal 2:", mamifero2.origen, mamifero2.especie, mamifero2.tipo, mamifero2.lugar)
print("Animal 3:", reptil.origen, reptil.especie, reptil.tipo, reptil.lugar)
print("Animal 4:", ave.origen, ave.especie, ave.tipo, ave.lugar)

