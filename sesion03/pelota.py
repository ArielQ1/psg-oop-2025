def envoltura(regalo):
  def papel():
    print("🎁🔖")
    regalo()
    print("🎁")
  return papel

@envoltura
def pelota():
  print("⚽")


pelota()

@envoltura
def chocolate():
  print("🍫")

chocolate()