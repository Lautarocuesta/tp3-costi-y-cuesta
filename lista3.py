
cofre1 = [10, 20, 30, 40, 50]
cofre2 = [20, 30, 40, 50, 60]

def monedascom(cofre1, cofre2):
  ccofre1 = set(cofre1)
  ccofre2 = set(cofre2)


  monedas_comunes = list(ccofre1.intersection(ccofre2))

  return monedas_comunes




monedascomun = monedascom(cofre1, cofre2)
print("Monedas en común en ambos cofres:", monedascomun)
