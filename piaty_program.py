samochody = ['syrena', 'polonez', 'opel']

print(samochody[0])
print(samochody[1])
print(samochody[2])

for s in samochody:
    print(s)

for idx in range( len(samochody) ):
    print("idx: " + str(idx) + " : " + samochody[idx])

samochody.append('mercedes')
samochody.append('fiat')
samochody.append('hyundai')

materialy_budowlane = ['cegla', 'cement']

print(materialy_budowlane[0])
print(materialy_budowlane[1])

for s in materialy_budowlane:
    print(s)

for idx in range( len(materialy_budowlane)):
    print("idx: " + str(idx) + " : " + materialy_budowlane[idx])

print ", " .join(materialy_budowlane)

imie = 'Ala'
zwierze = 'kot'
print("{0} ma {1}a" .format(imie, zwierze))
