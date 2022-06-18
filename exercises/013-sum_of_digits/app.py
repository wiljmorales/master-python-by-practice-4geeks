#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  sum = 0
  for digit in str(num):
    sum += int(digit)
  return sum


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))