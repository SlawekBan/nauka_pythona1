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
print('Do zaplacenia: ' + str(suma))
