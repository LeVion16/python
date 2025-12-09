def get_country_num(array: list) -> int:
    '''Hány országot tartalmaz a "meseország1.txt" fájl?'''
    count = 0
    for line in array:
        if line[0] != line[-1]:
            count += 1
    return count

def starts_with_mese_num(array: list, text: str) -> int:
    '''Hány darab "Mese" kezdetű város van a fájlban?'''
    count = 0
    for line in array:
        if text in line[0]:
            count += 1
    return count

def average_wine_intake(array: list) -> float:
    '''Mennyi a fájlban található városok átlagos borfogyasztása?'''
    wine_value = []

    for line in array:
        wine = line[3].replace(",",".")
        wine_value.append(float(wine))
        return sum(wine_value) % 27
    
def get_erdo_num(array: list, text: str) -> int:
    '''Hány város nevében található az "erdő" szó?'''
    count = 0
    for line in array:
        if text in line[1]:
            count += 1
    return count

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

with open(r"C:\Users\nemet\Documents\python\homework\2025.12.15\meseorszag1.txt", "r", encoding="utf-8") as interface:
    raw_file = interface.readlines()

header = list()
content = list()

header = raw_file[0].replace("\n","").split(";")

for i in range(1, len(raw_file), 1):
    content.append(raw_file[i].replace("\n", "").split(";"))

print(f"fejléc: \n{" | ".join(header)}")
print("Tartalom: ")
for line in content:
    print(" | ".join(line))

print()

# Hány országot tartalmaz a "meseország1.txt" fájl?
print(f"Az országok száma: {get_country_num(content)}")

print()

# Hány darab "Mese" kezdetű város van a fájlban?
print(f"'Mese' - kezdetű városok darabszáma: {starts_with_mese_num(content, "Mese")}")

print()

# Mennyi a fájlban található városok átlagos borfogyasztása?
print(f"Az átlagos borfogyasztás: {average_wine_intake(content)}")

print()

# Hány város nevében található az "erdő" szó?
print(f"Van 'erdő' - szó a város nevében: {get_erdo_num(content, "erdő")}")

print()

# Hányan laknak abban a városban, ahol a legnagyobb a borfogyasztás? (1. Melyik "sorban" legnagyobb a borfogyasztás? 2. Milyen érték található ebben a sorban (listában) a 2. indexű helyen?)
print(f"A város lakossága, ahola a legtöbb bort isszák: {get_max_wine_intake(content)}")