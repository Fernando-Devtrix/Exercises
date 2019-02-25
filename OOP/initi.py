class User:
  def __init__(self, nombre, last, age):
    self.name = nombre
    self.last = last
    self.age = age  
  
user1 = User("Fer", "Fuentes", 22)
print(user1.name)