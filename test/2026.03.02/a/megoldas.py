path = "./fuvar.csv"
f_content = list()
with open(path, "r", encoding="utf-8") as f:
    raw = f.readlines()
    
header = raw[0].strip().split(";")
for i in range(1, len(raw), 1):
    d = dict()
    line = raw[i].strip().split(";")
    d["taxi_id"] = int(line[0])
    d["indulas"] = line[1]
    d["idotartam"] = int(line[2])
    d["tavolsag"] = float(line[3].replace(",", "."))
    d["viteldij"] = float(line[4].replace(",", "."))
    d["borravalo"] = float(line[5].replace(",", "."))
    d["fizetes_modja"] = line[6]
    
    f_content.append(d)
    
# print(f_content)

# 6185-ös azonosítójú taxis bevétele, fuvarjainak száma:
def taxi_data(array: list, id: int) -> str:
    summa = 0
    count = 0
    for line in array:
        if line["taxi_id"] == id:
            summa += (line["viteldij"] + line["borravalo"])
            count += 1
    return f"A(z) {id} azonosítójú taxis bevétele: {summa} $, fuvarjainak száma: {count} db"
print(f"\n{taxi_data(f_content, 6185)}")

# összesen hány km-t tettek meg a taxisok (1 mérföld : 1,6 km) -- két tizedesjegy:
def summa_km(array: list) -> float:
    summa = 0
    for line in array:
        summa += line["tavolsag"]
    return round(summa * 1.6, 2)

print(f"\n Összesen {summa_km(f_content)} km-t tettek meg a taxisok.")

# Határozza meg, és írja ki a képernyőre, a minta szerint, hogy 15-én hányan fizettek bankkártyával!

def count_paying_instrument(array: list, instrument: str) -> int:
    count = 0
    for line in array:
        if line["fizetes_modja"] == instrument and line["indulas"][8:10:1] == '15':
            count += 1
    return count

print(f"\nBankkártyával {count_paying_instrument(f_content, "bankkártya")} utas fizetett.")

# írja ki a large.txt fájlba, a minta szerint, az időben leghosszabb fuvar adatait!
def large_transport(array: list) -> str:
    maximum = 0
    current_line = None
    for line in array:
        if line["tavolsag"] >  maximum:
            maximum = line["tavolsag"]
            current_line = line
    return f"{current_line["taxi_id"]};{current_line["indulas"]};{current_line["idotartam"]};{current_line["tavolsag"]};{current_line["viteldij"]};{current_line["borravalo"]};{current_line["fizetes_modja"]}"

with open("./large.txt", "w", encoding="utf-8") as f:
    print(large_transport(f_content), file=f)

# Határozza meg, és írja ki a képernyőre, a minta szerint, hogy volt-e olyan eset, amikor a megtett távolság nulla mérföld. A keresést csak addig folytassa, amíg nem talál ilyen esetet!

k = 0
while k < len(f_content) and f_content[k]["tavolsag"] != 0:
    k += 1
    
if k < len(f_content):
    print("\nVolt olyan eset, amikor a megtett távolsá 0 mérföld volt.\n")
else:
    print("\nNem volt olyan eset, amikor a megtett távolsá 0 mérföld volt.\n")