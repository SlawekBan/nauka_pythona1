produkt = 'mleko'
suma = 301

if 100 < suma and suma < 200:
    print('Promocja 30%!')
    suma = suma - (suma * 30) / 100
elif suma >= 200:
    print('Promocja 35%')
    suma = suma - (suma * 35) / 100
elif suma >= 300:
    print('Pomocja 50%')
    suma = suma - (suma * 50) / 100
else:
    print('bez promocji!')

print('Do zaplacenia ' + str(suma))
