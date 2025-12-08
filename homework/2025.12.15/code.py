# Hány országot tartalmaz a "meseország1.txt" fájl?
def get_country_num(array: list) -> int:
    count = 0
    for line in array:
        if line[0] != line[-1]:
            count += 1
    return count

# Hány darab "Mese" kezdetű város van a fájlban?
def starts_with_mese_num(array: list, text: str) -> int:
    count = 0
    for line in array:
        if text in line[0]:
            count += 1
    return count

# Mennyi a fájlban található városok átlagos borfogyasztása?
def average_wine_intake(array: list) -> float:
    total = 0.0
    count = 0
    for line in array:
        # Borfogyasztás (line[3]) tizedes , → . alakítás
        value = float(line[3].replace(",", "."))
        total += value
        count += 1
    return total / count


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