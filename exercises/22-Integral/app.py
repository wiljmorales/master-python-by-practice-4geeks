integer = int(input("Dime tu numero: "))


def integral(num):
  output = {}
  for i in range(1, num +1):
    output[f"{i}"] = i * i
  return output 

print(integral(integer))