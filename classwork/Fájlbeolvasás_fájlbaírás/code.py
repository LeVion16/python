path = "./cb.csv"
header = list()
content = list()

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

""" 
print(header)
for i in content:
    print(i) 
"""

# 3. Feladat
def get_registration_num(array: list) -> int:
    '''Megszámolja a bejegyések számát'''
    count = 0
    for line in array:
        count += 1
    return count

print(f"Összesen a bejegyzések száma: {get_registration_num(content)}")

# 4. Feladat
def start_radio_signal(content: list, count: int) -> bool:
    i = 0
    while len(content) > i and content[i]["AdasDb"] != count:
        i += 1
        
    if len(content) > i:
        return True
    return False
    
print(f"Van olayn sofőr aki 1 perc alatt pontosan 4 adást indított:  {start_radio_signal(content, 4)}")

# 5. Feladat
def get_calls_num(array: list, name: str) -> int:
    calls = 0
    for line in array:
        if name == line["Nev"]:
            calls += line["AdasDb"]
    return calls

print(f"A sofőr által indított hívások száma: {get_calls_num(content, "Tomi")}")

# 6. Feladat
def get_mins(hour: int, min: int) -> int:
    return hour * 60 + min

# 7. Feladat
output = ["Percek;AdasDb;Nev"]
for line in content:
    output.append(f'{get_mins(line["Ora"], line["Perc"])};{line["AdasDb"]};{line["Nev"]}')
    
with open("./min.txt", "w", encoding="utf-8") as new_File:
    for line in output:
        print(line, file=new_File)
    
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