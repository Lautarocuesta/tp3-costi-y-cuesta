cristales = ["oro", "oro","plata", "plata", "bronce", "diamante", "esmeralda"]

def deletecristales(lista):
    listaconduplicados = list(set(lista))
    return listaconduplicados

cristalesdu = deletecristales(cristales)
print("Cristales sin duplicados son :", cristalesdu)