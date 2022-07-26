#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  minutes = secs // 60
  hours = minutes // 60
  minutes = minutes % 60
  return (hours, minutes)

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))