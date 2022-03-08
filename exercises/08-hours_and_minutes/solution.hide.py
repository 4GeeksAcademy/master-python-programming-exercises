#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  hours = secs // 3600
  mins = secs // 60
  while (mins > 59):
    hours += 1
    mins -= 60
  
  
  return (hours, mins)
