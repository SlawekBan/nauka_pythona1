produkty = {'S1222': 'sukienka trojka',
            'P1222': 'spodnie krata',
            'X212':   'konsola do gier'}

igla = 'X2X'

if igla in produkty:
    print("Znalazlem {0}" .format(igla))
else:
    print("Brak w magazynie {0}" .format(igla))
