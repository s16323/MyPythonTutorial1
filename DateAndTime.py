# moduły time i datetime
import time

# print("Start")
# time.sleep(3)  # seconds - .sleep zatrzymuje całkowicie, to bardzo prosta i nieefektywna funkcja
# print("Stop")

while True:
    print("UNIX time is now:", time.time(), "seconds", "\n")        # zwraca UNIXowy czas - ilość sekund od 01.01.1970
    print("[q] for Quit or wait for:")
    waitFor = input()
    if waitFor == "q": break
    else: waitFor = int(waitFor)
    timer = time.time()
    time.sleep(waitFor)
    elapsed = time.time() - timer
    print(elapsed, "seconds passed")
    print("program delay was:", elapsed - waitFor, "\n")

# podawanie aktualnej daty i godziny:
print("\n", "----------Podawanie aktualnej daty i godziny:------------", "\n")

import datetime

data = datetime.datetime.now()  # aktualna data i godzina
rok = data.year
miesiac = data.month
dzien = data.day
godz = data.hour
minuty = data.minute
sekundy = data.second

czas = data.time()

print("\n",
        rok, type(rok), "\n",
        miesiac, type(miesiac), "\n",
        dzien,"\n",
        godz,"\n",
        minuty ,"\n",
        sekundy,"\n",
        data, type(data), "\n",
        czas, type(czas), "\n")

# string formated time Hour:Minute:day:month:Year...
print(data.strftime("%H:%M %d.%m.%Y"), type(data.strftime("%H:%M %d.%m.%Y")))

# 'H' zamienić na 'I' zeby był system 12-godzinny (%p - podaje AM lub PM)
# %b - podaje miesiąc słownie