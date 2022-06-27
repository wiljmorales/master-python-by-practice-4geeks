user_input = input("escribe una secuencia de numeros enteros separados por comas: ")

def to_touple (string):
  integer_list  = string.rstrip().rsplit(',')
  return tuple(integer_list)

print(to_touple(user_input))