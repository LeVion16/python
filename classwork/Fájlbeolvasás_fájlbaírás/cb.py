# 1. fel. Beolvasás
path = "./cb.csv"
fcontent = list()
raw = list()
with open(path, "r", encoding="utf-8") as f:
    raw = f.readlines()

header = raw[0].strip().split(";")
for i in range(1, len(raw), 1):
    line = raw[i].strip().split(";")
    d = dict()
    d["Ora"] = int(line[0])
    d["Perc"] = int(line[1])
    d["AdasDb"] = int(line[2])
    d["Nev"] = line[3]
    fcontent.append(d)
    
# print(header)
# print(fcontent)

# 3. fel. Volt-e 4 adás indító sofőr (egy percen belül)
def start_radio_signal(content: list, count: int) -> bool:
    i = 0
    while len(content) > i and content[i]["AdasDb"] != count:
        i += 1
        
    if len(content) > i:
        return True
    return False

if start_radio_signal(fcontent, 4):
    print("Volt négy adás indító sofőr.")
else:
    print("Nem volt négy adás indító sofőr.")
    
# 4. fel. Adott nevű sofőr hívásainak száma:
def summa_call_of_driver(content: list, name: str) -> int:
    summa = 0
    for line in content:
        if line["Nev"] == name:
            summa += line["AdasDb"]
    return summa 

n = input("Kérem egy sofőr nevét: ")   
result = summa_call_of_driver(fcontent, n)
if result:
    print(f"4. feladat: {n} nevű sorfőr hívásainak száma: {result}")
else:
    print(f"4. feladat: {n} nevű sorfőr nem létezik.")
    
# 5. feladat óra + perc = perc -- min.txt fájlba írás
def total_minutes(hour: int, min: int) -> int:
    return hour * 60 + min

output = ["Percek;AdasDb;Nev"]
for line in fcontent:
    output.append(f'{total_minutes(line["Ora"], line["Perc"])};{line["AdasDb"]};{line["Nev"]}')
    
with open("./min.txt", "w", encoding="utf-8") as newFile:
    for line in output:
        print(line, file=newFile)
        #newFile.writelines(line+"\n",)
        
# Összes adás átlaga:
def get_average(content: list) -> float:
    summa = 0
    for line in content:
        summa += line["AdasDb"]
    return summa / len(content)

average = get_average(fcontent)
result = round(average, 1)

# print(f"Hívások darabszámának átlaga: {average:.1f}")
print(f"Hívások darabszámának átlaga: {result}")