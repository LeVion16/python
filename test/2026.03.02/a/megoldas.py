# A program kérjen be a felhasználótól egysornyi, csillaggal tagolt adatot...

data = input("Adja meg az adatait csillag-karakterrel tagolva: ")
data_list = data.split("*")
data_end = data_list[-1].replace(".","-")

output = f"{data_list[0]};{data_list[1]};{data_list[2]};{data_list[3].replace(".","-")}"
# print(output)

with open("./user.txt", "w", encoding="utf-8") as f:
    print( output, file=f)
    
# Fájlbeolvasás:
    
path = "./orvosi_nobeldijak.csv"
f_content = list()
with open(path, "r", encoding="utf-8") as f:
    raw = f.readlines()

header = raw[0].strip().split(";")

for i in range(1, len(raw), 1):
    line = raw[i].strip().split(";")
    d = dict()
    d["Év"] = int(line[0])
    d["Név"] = line[1]
    d["SzületésHalálozás"] = line[2]
    d["Országkód"] = line[3]
    f_content.append(d)
    
# print(f_content)

# Határozza meg, és írja ki a képernyőre, hogy hány, ma már nem élő díjazott adatai találhatóak a forrásállományban!
def dead_nobels(array: list) -> int:
    count = 0
    for line in array:
        if len(line["SzületésHalálozás"]) == 5:
            count += 1
    return count

print(f"\nMa már nem élő díjazottak száma: {dead_nobels(f_content)} fő.")

# Határozza meg és írja a képernyőre, hogy az adatforrásban melyik volt az utolsó (legnagyobb) díjátadó éve, amelyben a díjazott(ak) adatait rögzítették!

def last_year(array: list) -> int:
    last = 0
    for line in array:
        if last < line["Év"]:
            last = line["Év"]
    return last

print(f"\nUtolsó év: {last_year(f_content)}")
    
# Kérje be a felhasználótól egy ország kódját! Ha a megadott országból nem volt díjazott, akkor „A megadott országból nem volt díjazott!” szöveget írja ki, ha az országból csak egy díjazott volt, akkor jelenítse meg az adatait! Ha a keresett országból több orvosi Nobel-díjas is volt az évek során, akkor írja ki a számukat a következő minta szerint: „A megadott országból 3 fő díjazott volt!”.

code = input("\nKérem, adja meg egy ország kódját: ")

def count_code(array: list, code: str) -> int:
    count = 0
    for line in  array:
        if line["Országkód"] == code:
            count += 1
    return count

if count_code(f_content, code) > 1:
    print(f"\nA megadott országból {count_code(f_content, code)} fő díjazott volt.")
elif count_code(f_content, code) == 1:
    print(f"\tA megadott ország díjazottja: ")
    k = 0
    while f_content[k]["Országkód"] != code:
        k += 1
    print(f"\tNév: {f_content[k]["Név"]}")
    print(f"\tÉv: {f_content[k]["Év"]}")
    print(f"\tSz/H: {f_content[k]["SzületésHalálozás"]}")
else:
    print("\nA megadott országból nem volt díjazott.")