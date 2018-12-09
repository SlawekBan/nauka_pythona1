samolot = {'name': 'boeing',
            'przebieg': 10000,
            'type': 'pasazerski'}

#print(samolot['name'])
#print(samolot['type'])

# co wypiszemy na ekran
#print(samolot['nieznany_klucz'])

# in python 3 samolot.item()
for key, value in samolot.iteritems():
    print("{0}:{1}".format(key, value))

#
for key in samolot:
    print("{0}:{1}".format(key, samolot[key]))

print('--------------')

koszyk = [
    {'name': 'mleko', 'cena': 12.5},
    {'name': 'ser', 'cena': 4.0},
    {'name': 'konsola gier', 'cena': 114.0}
]

print(koszyk[0]['cena'])
print(koszyk[1]['cena'])
print(koszyk[2]['cena'])

suma_koszyka = (koszyk[0]['cena']+koszyk[1]['cena']+koszyk[2]['cena'])


print('Suma koszyka wynosi = ' + str(suma_koszyka))
#mleko i ser => 10%
stan_reguly = {'mleko': False,
                'ser': False}

#bylo_mleko = False

suma = 0
for poz in koszyk:
    suma = suma + poz['cena']
    nazwa_prod = poz['nazwa']
    if nazwa_prod == 'mleko' or nazwa_prod == 'ser':
        stan_reguly[nazwa_prod] = True
    if stan_reguly['mleko'] and stan_reguly['ser']:
        print('znizka')
    suma = suma + (suma * 10) / 100
print("Wartosc koszyka= " + str(suma))
#        bylo_mleko = True

#if bylo_mleko == True:
#    print('Znizka!!!')
#    suma = suma - (suma * 10) / 100

#print(suma)

#promocja_koszyka = (koszyk[0]['cena']+koszyk[1]['cena'])
#print(promocja_koszyka)
#for promocja_koszyka
