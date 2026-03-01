path = "./csongrad.txt"
content = []
header = list()
with open(path, "r", encoding="utf-8") as f:
    raw = f.readlines()
    
header = raw[0].strip().split("\t")

for i in range(1, len(raw)):
    line = raw[i].strip().split("\t")
    d = dict()
    d["Megnevezés"] = line[0]
    d["Jogállás"] = line[1]
    d["Járás"] = line[2]
    d["Terület (ha)"] = int(line[3])
    d["Lakosság"] = int(line[4])
    content.append(d)
    
# Adatsorok száma:
print(f"1 feladat: A fájlban {len(content)} bejegyzés található.")

# Csongrád megye lakosságának átlaga 2 tizedesjegy pont.
def get_average(cont: list) -> float:
    summa = 0
    for line in cont:
        summa += line["Lakosság"]
    return summa/len(cont)

rounded_result = round(get_average(content), 2)

print(f"Csongrád megye lakosságának átlaga: {get_average(content):.2f}")

# Község jogállású települések lakossága:
def summa_people(cont: list, conditional: str) -> int:
    summa = 0
    for line in cont:
        if line["Jogállás"] == conditional:
            summa += line["Lakosság"]
    return summa

print(f"Lakosok száma {summa_people(content, "község")} fő")

# falva vagy halom vgű községek adatai -> text.txt fájlba (;)
def search_village(cont: list, end1: str, end2: str) -> list:
    result = []
    for line in cont:
        if line["Jogállás"] == "község":
            if line["Megnevezés"].endswith(end1) or line["Megnevezés"].endswith(end2):
                result.append(f"{line["Megnevezés"]};{line["Jogállás"]};{line["Járás"]};{line["Terület (ha)"]};{line["Lakosság"]}")
    return result

result_list = search_village(content, "falva", "halom")
print(result_list)

with open("./text.txt", "w", encoding="utf-8") as f:
    for line in result_list:
        print(line, file=f)
        
# Statisztika a településfajták lakosságáról:
def statistic(cont: list) -> dict[str, int]:
    myDict = dict()
    for line in cont:
        if line["Jogállás"] in myDict.keys():
            myDict[line["Jogállás"]] += 1
        else:
            myDict[line["Jogállás"]] = 1
    return myDict

result2 = statistic(content)
# Szép kiíráshoz:
print("Csongrád vármegye településeinek statisztikája:")
for key in result2.keys():
    print(f"\t{key}: {result2[key]} db")
    
# Legkisebb lakosszámú város adatai -> city.txt ("|")
def lowesd(cont: list) -> str:
    smollest = cont[0]["Lakosság"]
    row = cont[0]
    for i in range(1, len(cont), 1):
        if cont[i]["Jogállás"] == "város":
            if smollest > cont[i]["Lakosság"]:
                smollest = cont[i]["Lakosság"]
                row = cont[i]
    return f"{row["Megnevezés"]}|{row["Jogállás"]}|{row["Járás"]}|{row["Terület (ha)"]}|{row["Lakosság"]}"
with open("./city.txt", "w", encoding="utf-8") as f:
    print(lowesd(content), file=f)
    
# A megadott település (ha létezik) lakosságszámát írja ki a program:
input_value = input("Adja meg egy település nevét: ")
result3 = None
for line in content:
    if line["Megnevezés"] == input_value:
        result3 = line["Lakosság"]
if result3:
    print(f"A {input_value} település lakosainak száma: {result3} fő.")
else:
    print(f"A megadott '{input_value}' település nem létezik.")