# Definiendo la clase
class Persona:
  def __init__(self, nombre): # Constructor
    self.nombre = nombre
    self.hambre = True
 
  def saludar(self): # Método de instancia
    print(f"Hola, soy {self.nombre}")

  def dormir(self, horas): # Nuevo Método de instancia
    print(f"{self.nombre} duerme por {horas} hrs.")
    print(f"{self.nombre} se ha despertado")
    self.hambre = True

  def comer(self, comida): # Nuevo Método de instancia
    if self.hambre:
      print(f"{self.nombre} está comiendo {comida}")
      self.hambre = False
      return "🍽️"
    else:
      print(f"{self.nombre} no tiene hambre")
      return comida

jhon = Persona("Jhon")

# Llamando al método de la instancia
# jhon.saludar()
# # Llamando al método de la instancia
# jhon.dormir(8)
# comida = jhon.comer("🍕")
# print(f"Devolvió: {comida}")
# comida = jhon.comer("🍔")
# print(f"Devolvió: {comida}")
# jhon.dormir(1)
# comida = jhon.comer("🍔")
# print(f"Devolvió: {comida}")

print ("======")
class Perro:
  factor_edad = 7 # Atributo de clase
  def __init__(self, nombre, edad): # Constructor
    self.nombre = nombre
    self.edad = edad

  def ladrar(self): # Método de instancia
    print(f"{self.nombre} dice: ¡Guau!")

  def crecer(self, tiempo): # Método de instancia
    self.edad += tiempo
    print(f"{self.nombre} ha crecido {tiempo} años")

  @classmethod # Nuevo Método de clase
  def nacer(cls, nombre):
    print(f"{nombre} ha nacido como un cachorro")
    return cls(nombre,0)

  @classmethod # Nuevo Método de clase
  def edad_a_humano(cls, perro):
    print(f"En años humanos, {perro.nombre}")
    print(f"tiene {perro.edad * cls.factor_edad} años")

# rex = Perro.nacer("Rex")
# rex.ladrar()
# rex.crecer(2)
# rex.crecer(2)
# Perro.edad_a_humano(rex)

# Definiendo la clase
class Gato:
  def __init__(self, nombre, color): # Constructor
    self.nombre = nombre
    self.color = color
    self.edad = 0
  
  @classmethod # Método de clase
  def nacer(cls, nombre, color):
    print(f"{nombre} ha nacido como un cachorro")
    return cls(nombre, color)

  def crecer(self, tiempo): # Método de instancia
    self.edad += tiempo
    print(f"{self.nombre} ha crecido {tiempo} años")

  def maullar(self): # Método de instancia
    print(f"{self.nombre} dice: {Gato.sonidos()[0]}")

  @staticmethod # Nuevo Método estático
  def sonidos():
    return ["miau", "ronroneo"]

# Instanciando un objeto
mimi = Gato.nacer("Mimi", "blanco")
mimi.maullar()
mimi.crecer(2)
sonidos = Gato.sonidos()
print(f"Sonidos de {mimi.nombre}: {sonidos}")