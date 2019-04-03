# napisac program ktory rozbija podana kwote na minimalna liczbe banknotow i monet;

# nominaly: 200 100 50 20 10 5 2 1

licznik = int(input('podaj kwote: '))
print('kwota:', licznik)

# banknoty 200:
dwusetki = 0
while licznik >= 200:
    dwusetki += 1
    licznik = licznik - 200

# banknoty 100:
setki = 0
while licznik >= 100:
    setki += 1
    licznik = licznik - 100

# banknoty 50:
piecdziesiatki = 0
while licznik >= 50:
    piecdziesiatki += 1
    licznik = licznik - 50

# banknoty 20:
dwudziestki = 0
while licznik >= 20:
    dwudziestki += 1
    licznik = licznik - 20

# banknoty 10:
dziesiatki = 0
while licznik >= 10:
    dziesiatki += 1
    licznik = licznik - 10

# monety 5:
piatki = 0
while licznik >= 5:
    piatki += 1
    licznik = licznik - 5

# monety 2:
dwojki = 0
while licznik >= 2:
    dwojki += 1
    licznik = licznik - 2

# monety 1:
jedynki = 0
while licznik >= 1:
    jedynki += 1
    licznik = licznik - 1


# print('200:', dwusetki, '\n',
#     '100:', setki, '\n',
#     '50:', piecdziesiatki, '\n',
#     '20:', dwudziestki, '\n',
#     '10:', dziesiatki, '\n',
#     '5:', piatki, '\n',
#     '2:', dwojki, '\n',
#     '1:', jedynki, '\n'
#       )




