# 2. feladat: Beolvasás univerzálisan
# A fájl neve nálad a zip-ben berek.csv volt
datas = []
with open("./berek.csv", "r", encoding="utf-8") as text:
    # A fejlécet külön elmentjük egy listába
    header = text.readline().strip().split(";")
    
    # A maradék sorokon végigmegyünk
    for line in text:
        # Tisztítás és darabolás
        sor = line.strip().split(";")
        
        # Szótár készítése a megadott kulcsokkal
        # Név;Neme;Részleg;Belépés;Bér
        dolgozo = {
            header[0]: sor[0],
            header[1]: sor[1],
            header[2]: sor[2],
            header[3]: sor[3],
            header[4]: sor[4]
        }
        datas.append(dolgozo)

# 4. feladat: Fejléc mezőneveinek kiírása
print("4. feladat: A fájl fejléce:")
print(", ".join(header))

# 5. feladat: Keresztnév bekérése
keresett_nev = input("5. feladat: Kérlek, adj meg egy keresztnevet: ")

# a. Dolgozók kilistázása, akiknek ez a keresztneve
# b. Fizetések összege
# c. Legkorábban belépő keresése
talalt_dolgozok = []
osszes_ber = 0
legregebbi_dolgozo = None

for d in datas:
    # Megnézzük, hogy a név tartalmazza-e a keresztnevet (pl. "Sipos Gábor"-ban benne van-e a "Gábor")
    if keresett_nev in d["Név"]:
        talalt_dolgozok.append(d["Név"])
        osszes_ber += int(d["Bér"])
        
        # Minimumkeresés a belépési év alapján
        if legregebbi_dolgozo is None or int(d["Belépés"]) < int(legregebbi_dolgozo["Belépés"]):
            legregebbi_dolgozo = d

# Eredmények kiírása a minta szerint
print(f"\nA(z) {keresett_nev} nevű dolgozók:")
for nev in talalt_dolgozok:
    print(nev)

print(f"\nA(z) {keresett_nev} nevű dolgozók fizetésének összege: {osszes_ber} Ft")

if legregebbi_dolgozo:
    print(f"\nA(z) {keresett_nev} nevű dolgozók közül a legkorábban belépő:")
    print(f"{legregebbi_dolgozo['Név']}, belépésének éve: {legregebbi_dolgozo['Belépés']}")