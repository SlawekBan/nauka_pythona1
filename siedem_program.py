samolot = {'name': 'boeing',
            'przebieg': 10000,
            'type': 'pasazerski'}
# in python 3 samolot.item()
for key, value in samolot.iteritems():
    print("{0}:{1}".format(key, value))

#
for key in samolot:
    print("{0}:{1}".format(key, samolot[key]))
