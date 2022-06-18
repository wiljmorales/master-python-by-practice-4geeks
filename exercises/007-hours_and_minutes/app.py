#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  output = (secs // 3600, (secs % 3600) // 60)
  return output

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))