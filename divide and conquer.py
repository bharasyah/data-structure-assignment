a = [12,45,6,3,7,34,24,26,]

def maks(list):
  max = list[0]

  for i in list:
    if i > max:
      max = i

  return max

def min(list):
  z = list[0]

  for i in list:
    if i < z:
      z = i

  return z

print('Nilai terbesar:', maks(a))
print('Nilai terkecil:', min(a))