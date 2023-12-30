def hours_minutes(seconds):
  # Your code here
  hours = seconds // 3600
  remaining_seconds = seconds % 3600
  minutes = remaining_seconds // 60
  return (hours, minutes)

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
