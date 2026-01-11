with open(r"C:\Users\nemet\Documents\python\Practice\Doga_gyak1\meseiskola.txt", "r", encoding="UTF-8") as interface:
    raw_file = interface.readlines()

header = list()
content = list()

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

def get_males(array: dict) -> int:
    max_num = 0
    for i in array:
        max_num += int(i["Fiúk száma"])
    return max_num

print(get_males(content))

def get_name(array: dict) -> int:
    count = 0
    for line in array:
        if "Nagy" in line["Osztályfőnök"]:
            count += 1
    return count

print(get_name(content))

def get_5th_num(array: dict) -> int:
    num = 0
    for line in array:
        if "5" in line["Osztály"]:
            num = line["Fiúk száma"] + line["Lányok száma"]
    return num

print(get_5th_num(content))

def get_name_by_class(array: list) -> str:
    max_students = 0
    name = ""
    for row in array:
        total = int(row["Fiúk száma"]) + int(row["Lányok száma"])
        if total > max_students:
            max_students = total
            name = row["Osztályfőnök"]
    return name

print(get_name_by_class(content))

def count_worse_than_4(array: dict) -> int:
    count = 0
    for i in array:
        avg = float(row["Tanulmányi Átlag"].replace(",", "."))
        if avg < 4.0:
            count += 1
    return count

print(count_worse_than_4(content))

def total_students_with_judit(array: list) -> int:
    total = 0
    for row in array:
        if "Judit" in row["Osztályfőnök"]:
            total += int(row["Fiúk száma"]) + int(row["Lányok száma"])
    return total

print(total_students_with_judit(content))