# 1.Feladat
# 2.Feladat
header = list()
content = list()
path = "./cb.csv"
with open(path, "r", encoding="UTF-8") as raw:
    file = raw.readlines()

header = file[0].strip().split(";")
for i in range(1, len(file), 1):
    line = file[i].strip().split(";")
    d = dict()
    d["Ora"] = int(line[0])
    d["Perc"] = int(line[1])
    d["AdasDb"] = int(line[2])
    d["Nev"] = line[3]
    content.append(d)

'''
print(header)
for i in content:
    print(i)
'''

# 3.Feladat
def get_regritstation_num(array: list) -> int:
    count = 0
    for i in array:
        count += 1
    return count

print(f"Bejegyzések száma: {get_regritstation_num(content)}")

# 4.Feladat
def get_radio_signal(array: list) -> bool:
    i = 0
    while len(array) > 0 and array[i]["AdasDb"] != 4:
        i += 1

    if len(content) > i:
        return True
    return False

if get_radio_signal(content) == True:
    print("Volt négy adást indító sofőr")
else:
    print("Nem volt négy adást indító soför")

# 5.Feladat
def get_using_num(array: list, name: str) -> int:
    use = 0
    for line in array:
        if line["Nev"] == name:
            use += line["AdasDb"]
    return use

name = input("kérek egy nevet: ")
print(f"{name} 34x használt a CB-rádiót.")

# 6.Feladat
def get_min(hour: int, min: int) -> int:
    return hour * 60 + min

# 7.Feladat
output = ["Perc;AdasDb; Nev"]
for line in content:
    output.append(f'{get_min(line["Ora"], line["Perc"])}; {line["AdasDb"]}; {line["Nev"]}')

with open("min.txt", "w", encoding="UTF-8") as new_file:
    for line in output:
        print(line, file=new_file)

# 8. Feladat
def get_pilots_num(array: list) -> int:
    names = []
    for line in array:
        names.append(line["Nev"])

    count = 0
    for n in range(len(names)):
        if n in names:
            continue
        else:
            count += 1

    return count

print(f"Sofőrök száma: {get_pilots_num(content)}")