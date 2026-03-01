path = './csongrad.txt'
with open(path, "r", encoding="UTF-8") as raw:
    file = raw.readlines()

header = list()
header = file[0].strip().split('\t')

content = list()
for i in range(1, len(file), 1):
    line = file[i].strip().split('\t')
    d = dict()
    d['Megnevezés'] = line[0]
    d['Jogállás'] = line[1]
    d['Járás'] = line[2]
    d['Terület (ha)'] = int(line[3])
    d['Lakosság (fő)'] = int(line[4])
    content.append(d)

# 1.Feladta -> Adatsorok száma
print(f'1: Feladat -> A fájlban {len(content)} bejegyzés található.')

# 2.Feladat -> Csongrád megye lakosságának átlaga 2 tizedesjegy pontosságig.
def get_average(array: list) -> float:
    summa = 0
    for line in array:
        summa += line["Lakosság (fő)"]
    return summa/len(array) #összes lakosság osztva a települések számával

print(f'2.Feladat -> Csongrád megye lakosságának átlaga: {get_average(content):.2f}')

# 3.Feladat ->  Község jogállású települések lakossága
def get_village_population(array: list) -> int:
    summa = 0
    for line in array:
        if line['Jogállás'] == 'község':
            summa += line['Lakosság (fő)']
    return summa

print(f'3.Feladat -> Község jogállású települések lakossága: {get_village_population(content)}')

# 4.Feladat -> 'falva' vagy 'halom' végződésű községek adatai -> text.txt fájlba
def search_village(array: list) -> list:
    result = list()
    for line in array:
        if line['Jogállás'] == 'község':
            if line['Megnevezés'].endswith('falva') or line['Megnevezés'].endswith('halom'):
                result.append(line["Megnevezés"])
    return result

with open("./text.txt","w", encoding='UTF-8') as f:
    for line in search_village(content):
        print(line, file=f)

# 5.Feladat -> Statisztika a településfajták lakosságáról
def statistic(array: list) -> dict:
    d = dict()
    # Végigmegyünk a listánk minden egyes elemén
    for line in array:
        # Megnézzük, hogy az adott "Jogállás" (pl. 'város') már benne van-e a szótárban
        if line["Jogállás"] in d.keys():
            # Ha igen, növeljük a számát 1-gyel
            d[line["Jogállás"]] += 1
        else:
            # Ha még nincs benne, felvesszük a szótárba 1-es értékkel
            d[line["Jogállás"]] = 1
    return d

print(f'5.Feladat -> Statisztika a településfajták lakosságáról: {statistic(content)}')

# 6.Feladat -> Legkisebb lakosszámú város adatai -> city.txt fájlba
def lowesd(array: list) -> str:
    # Kikeressük az első várost a kezdőértéknek
    smallest_city = None
    for line in array:
        if line["Jogállás"] == "város":
            smallest_city = line
            break

    # Végigmegyünk a listán és összehasonlítjuk a lakosságszámokat
    for line in array:
        if line["Jogállás"] == "város":
            if line["Lakosság (fő)"] < smallest_city["Lakosság (fő)"]:
                smallest_city = line
                
    # 3. Formázzuk a kimenetet
    return f"{smallest_city['Megnevezés']}|{smallest_city['Jogállás']}|{smallest_city['Járás']}|{smallest_city['Terület (ha)']}|{smallest_city['Lakosság (fő)']}"

with open("./city.txt", "w", encoding="utf-8") as f:
    f.write(lowesd(content))

# A megadott település (ha létezik) lakosságszámát írja ki a program:
input_value = input("Adja meg egy település nevét: ")
result3 = None

# Végigmegyünk a listán
for line in content:
    # Megnézzük, hogy egyezik-e a név
    if line["Megnevezés"] == input_value:
        result3 = line["Lakosság (fő)"]
        break # Ha megtaláltuk, nem kell tovább keresni

if result3:
    print(f"A {input_value} település lakosainak száma: {result3} fő.")
else:
    print(f"A megadott '{input_value}' település nem létezik.")