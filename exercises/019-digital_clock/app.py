# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
def digital_clock(n):
  horas = n // 60
  minutos = n % 60

  return horas, minutos

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(150))

