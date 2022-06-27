class My_Class():
  def __init__(self):
    self.name = ""

  def getString(self):
    self.name = input("introduce un string: ")

  def printString(self):
    return self.name.upper()

prueba = My_Class()

prueba.getString()
print(prueba.printString())