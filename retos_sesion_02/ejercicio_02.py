class Vino:
  def __init__(self, nombre, tipo, cepa, anioProduccion):
    self.nombre = nombre
    self.tipo = tipo
    self.cepa = cepa
    self.anioProduccion = anioProduccion
    
class Queso:
  def __init__(self, nombre, variedad, edad, llevaSal):
    self.nombre = nombre
    self.variedad = variedad
    self.edad = edad
    self.llevaSal = llevaSal

print("---Vinos y quesos encontrados---")
vino1 = Vino("Malbec", "tinto", "Malbec", 2020)
vino2 = Vino("Chardonnay", "blanco", "Chardonnay", 2019)
vino3 = Vino("Cabernet Sauvignon", "tinto", "Cabernet Sauvignon", 2018)
vino4 = Vino("Sauvignon Blanc", "blanco", "Sauvignon Blanc", 2021)
queso1 = Queso("Cheddar", "Cheddar", 12, True)
queso2 = Queso("Brie", "Brie", 4, False)
queso3 = Queso("Gouda", "Gouda", 6, True)

print("Vino 1:", vino1.nombre, vino1.tipo, vino1.cepa, vino1.anioProduccion)
print("Vino 2:", vino2.nombre, vino2.tipo, vino2.cepa, vino2.anioProduccion)
print("Vino 3:", vino3.nombre, vino3.tipo, vino3.cepa, vino3.anioProduccion)
print("Vino 4:", vino4.nombre, vino4.tipo, vino4.cepa, vino4.anioProduccion)
print("Queso 1:", queso1.nombre, queso1.variedad, queso1.edad, queso1.llevaSal)
print("Queso 2:", queso2.nombre, queso2.variedad, queso2.edad, queso2.llevaSal)
print("Queso 3:", queso3.nombre, queso3.variedad, queso3.edad, queso3.llevaSal)