def hours_minutes(seconds):
  # Your code here
  return (int(seconds/3600), int((seconds%3600)/60))

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
