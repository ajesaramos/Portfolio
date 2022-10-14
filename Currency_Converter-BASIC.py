#From Platzy's "Curso Basico de Python"
#Convert n Chilean pesos to USD
#FURTHER: top 5 currencies. Top 3 cryptos. From a to b and viceversa.

pesos = input("Cuantos CLP quieres convertir?")
pesos = int(pesos)

valor_usd = 968

dolares = pesos / valor_usd

dolares = round(dolares,2)
dolares = str(dolares)
pesos = str(pesos)
print('$'+pesos+' pesos chilenos son: '+dolares+'USD')
