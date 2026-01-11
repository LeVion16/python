with open(r"C:\Users\nemet\Documents\python\Practice\Doga_gyak2\meseorszag1.txt", "r", encoding="utf-8") as interface:
    raw_file = interface.readlines()

header = list()
content = list()

header = raw_file[0].replace("\n", "").split(';')

for i in range(1, len(raw_file), 1):
    content.append(raw_file[i].replace("\n", "").split(";"))

print(" | ".join(header))
for line in content:
    print(" | ".join(line))

def get_country_num(array: list) -> int:
    '''Hány országot tartalmaz a fájl?'''
    count = 0
    for line in array:
        count += 1
    return count

print(get_country_num(content))

def get_start_wth_mese(array: list) -> int:
    '''Hány darab "Mese" kezdetű város van a fájlban?'''
    count = 0
    for line in array:
        if "Mese" in line[0]:
            count += 1
    return count

print(get_start_wth_mese(content))

def get_avg_wine_intake(array: list) -> float:
    '''Mennyi a fájlban található városok átlagos borfogyasztása?'''
    wine_value = []

    for line in array:
        wine = line[3].replace(",",".")
        wine_value.append(float(wine))
        return sum(wine_value) % 27

print(get_avg_wine_intake(content))

def get_town_by_name(array: list) -> int:
    '''Hány város nevében található "erdő" - szó?'''
    count = 0
    for line in array:
        if "erdő" in line[1]:
            count += 1
    return count

print(get_town_by_name(content))

def get_town_by_population(array: list) -> str:
    '''Melyik városnak van a legnépesebb lakossága? (Hol laknak legtöbben?)'''
    town = ''
    population = 0
    for line in array:
        if int(line[2]) > int(population):
            population = line[2]
            town = line[1]
    return town

print(get_town_by_population(content))

def get_max_wine_intake(array: list) -> int:
    '''Hányan laknak abban a városban, ahol a legnagyobb a borfogyasztás? (1. Melyik "sorban" legnagyobb a borfogyasztás? 2. Milyen érték található ebben a sorban (listában) a 2. indexű helyen?)'''
    max_intake = 0.0
    population = 0

    for line in array:
        if len(line) < 4:
            continue

        wine = line[3].replace(",",".")
        wine = float(wine)
        if wine > max_intake:
            population = line[2]
    return population

print(get_max_wine_intake(content))
