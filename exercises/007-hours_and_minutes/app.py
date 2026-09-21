def hours_minutes(seconds):
  # Your code here
  horas = seconds // 3600
  segundos_restantes = seconds % 3600
  minutos = segundos_restantes // 60
  
  return horas, minutos

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
