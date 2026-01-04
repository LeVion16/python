def get_male_num(array: dict) -> int:
    max_num = 0
    for i in array:
        max_num += int(i["Fiúk száma"])
    return max_num

def get_name_num(array: dict) -> int:
    num = 0
    for i in array:
        if "Nagy" in i["Osztályfőnök"]:
            num += 1
    return num
        
def get_5th_num(array: dict) -> int:
    max_num = 0
    for i in array:
        if "5" in i["Osztály"]:
            max_num = i["Fiúk száma"] + i["Lányok száma"]
    return max_num

def get_name_by_class(array: list) -> str:
    max_students = 0
    name = ""
    for row in array:
        total = int(row["Fiúk száma"]) + int(row["Lányok száma"])
        if total > max_students:
            max_students = total
            name = row["Osztályfőnök"]
    return name

def count_worse_than_4(array: list) -> int:
    count = 0
    for row in array:
        avg = float(row["Tanulmányi Átlag"].replace(",", "."))
        if avg < 4.0:
            count += 1
    return count

def total_students_with_judit(array: list) -> int:
    total = 0
    for row in array:
        if "Judit" in row["Osztályfőnök"]:
            total += int(row["Fiúk száma"]) + int(row["Lányok száma"])
    return total

def equal_boys_girls(array: list) -> list:
    result = []
    for row in array:
        if int(row["Fiúk száma"]) == int(row["Lányok száma"]):
            result.append(row["Osztály"])
    return result

def more_girls_than_boys(array: list) -> int:
    count = 0
    for row in array:
        if int(row["Lányok száma"]) > int(row["Fiúk száma"]):
            count += 1
    return count

with open(r"C:\Users\Menyk\Documents\python\homework\2026.01.04\meseiskola.txt", "r", encoding="utf-8") as interface:
    raw_file = interface.readlines()

header = []
content = []

header = raw_file[0].replace("\n", "").split(";")

for i in range(1, len(raw_file)):
    values = raw_file[i].replace("\n", "").split(";")
    row_dict = {}

    for j in range(len(header)):
        row_dict[header[j]] = values[j]

    content.append(row_dict)

print("Fejléc:")
print(" | ".join(header))

print("\nTartalom:")
for row in content:
    print(" | ".join(row.values()))

print()

print(get_male_num(content))

print()

print(get_name_num(content))

print()

print(get_5th_num(content))

print()

print(get_name_by_class(content))

print()

print(count_worse_than_4(content))

print()

print(total_students_with_judit(content))

print()

print(equal_boys_girls(content))

print()

print(more_girls_than_boys(content))