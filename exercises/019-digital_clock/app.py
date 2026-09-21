# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
import math

def digital_clock(n):
  return (math.floor(n/60), n%60)

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(1439))
