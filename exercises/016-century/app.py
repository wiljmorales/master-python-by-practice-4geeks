#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math
def century(year):
  if year % 100 == 0:
    return math.floor(year/ 100)
  return math.ceil(year/ 100)



#Invoke the function with any given year. 
print(century(1900))