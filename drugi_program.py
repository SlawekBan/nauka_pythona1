marka = 'Peugot'
marka1 = 'Peugot'
marka2 = 'Peugot'
ilosc_drzwi = 5
pojemnosc = 1.3
marka_up = marka.capitalize()
marka1_up = marka1.upper()
marka2_up = marka2.lower()

print("Samochod " + marka + " ma " + str(ilosc_drzwi) + " drzwi")
print(marka_up)
print(marka1_up)
print(marka2_up)
print("Pojemnosc po zmianach: " + str(pojemnosc * 2))
print(len(marka))

if ilosc_drzwi > 3:
    print('Duzy samochod!')
else:
    print('Maly')

if marka == 'Peugot':
    print('Samochod z Francji')
else:
    print('Inny')

print(marka[0:2])
