def hours_minutes(secs):
  # Your code here
  minutes = secs // 60
  hours = minutes // 60
  minutes = minutes % 60
  return (hours, minutes)

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
