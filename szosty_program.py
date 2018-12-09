samochody = ['syrena', 'polonez']
ilosc = [3 ,5]

for idx in range( len(samochody)):
    print("idx: " + str(idx) + ": " + samochody[idx])
    print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))


media = ['woda', 'prad']
cena = [20, 10]

for idx in range( len(media)):
    print("idx: " + str(idx) + ": " + media[idx])
    print(media[idx] + " ma cene " + str(cena[idx]))

print('-----------------------')

koszyk = ['herbata', 'kawa']
cena = [2, 3]
suma = sum(cena)
print('Cena bez promocji= ' + str(suma))

if cena > 3:
    print('Promocja 20%')
    suma = suma - (suma * 20) / 100

elif cena > 500:
    print('Pomocja 15')
    suma = suma - (suma * 15) / 100
print('Do zaplacenia: ' + str(suma))

print('---------------')

produkty = ['mleko']
ceny = [120, 320, 22]

suma = 0

for c in ceny:
    suma = suma + c

if suma > 500:
    print('20 % off, >500!')
    suma = suma - (suma * 20.0)/100

if len(produkty) > 3:
    print('000 Udane zakupy!')
    suma = suma - (suma * 15.0) / 1000

print("Do zaplaty: {0}".format(suma))
