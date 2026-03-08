# ---- 1.Feladat ----
path = './fuvar.csv'
with open(path, "r", encoding="UTF-8") as raw:
    file = raw.readlines()

header = list()
header = file[0].strip().split(";")

content = list()
for i in range(1, len(file), 1):
    line = file[i].strip().split(";")
    d = dict()
    d['taxi_id'] = int(line[0])
    d['indulas'] = line[1]
    d['idotartam'] = int(line[2])
    d['tavolsag'] = float(line[3].replace(",","."))
    d['viteldij'] = float(line[4].replace(",","."))
    d['borravalo'] = float(line[5].replace(",","."))
    d['fizetes_modja'] = line[6]
    content.append(d)

# ---- 2.Feladat ----
def get_6185_data(array: list) -> str:
    summa = 0
    rides = 0
    for line in array:
        if line['taxi_id'] == 6185:
            summa += line['viteldij'] + line['borravalo']
            rides += 1
    return f"A bevétel {summa} | a fuvarok száma: {rides}"

print(get_6185_data(content))

# ---- 3.Feladat ----
def get_distance_km(array: list) -> str:
    summa = 0
    for line in array:
        summa += line['tavolsag']
    return round(summa * 1.6, 2)

print(f'A taxisok összesen {get_distance_km(content)}km-et tettek meg.')

# ---- 4.Feladat ----
def get_pay_method(array: list) -> str:
    count = 0
    for line in array:
        if line['indulas'][8:10:1].startswith('15'):
            if line['fizetes_modja'] == "bankkártya":
                count += 1
    return f"15-én {count} személy fizetett bankkártyával."

print(get_pay_method(content))

# ---- 5.Feladat ----
def get_longest_ride(array: list) -> str:
    result = 0
    current_line = None
    for line in array:
        if line['idotartam'] > result:
            result = line['idotartam']
            current_line = line
    return f'{current_line["taxi_id"]};{current_line["indulas"]};{current_line["idotartam"]};{current_line["tavolsag"]};{current_line["viteldij"]};{current_line["borravalo"]};{current_line["fizetes_modja"]}'

with open('large.txt', "w", encoding="UTF-8") as f:
    print(get_longest_ride, file=f)

# ---- 6.Feladat ----

k = 0
while k < len(content) and content[k]["tavolsag"] != 0:
    k += 1
    
if k < len(content):
    print("\nVolt olyan eset, amikor a megtett távolsá 0 mérföld volt.\n")
else:
    print("\nNem volt olyan eset, amikor a megtett távolsá 0 mérföld volt.\n")