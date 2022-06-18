#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
  output = ""
  stringified_num = str(num)
  for i in range(len(stringified_num)):
    if stringified_num[i] == ".":
      output += stringified_num[i+1]
  return int(output)



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.23))