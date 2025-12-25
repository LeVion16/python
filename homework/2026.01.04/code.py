def get_male_number(array: dict) -> int:
    for line in array:
        

with open(r"C:\Users\nemet\Documents\python\homework\2026.01.04\meseiskola.txt", "r", encoding="utf-8") as interface:
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