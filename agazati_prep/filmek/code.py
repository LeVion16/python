print('1. feladat: Mozijegy-számítás')
age = int(input('Add meg az eletkorod: '))
price = int(input('Add meg a jegy alaparat (Ft): '))

discount = 0
if age < 14:
    discount = 50
elif age <= 18:
    discount = 30
elif age > 60:
    discount = 25
else:
    discount = 0

print(f'Kedvezmeny: {discount}%')
print(f'Fizetendo osszeg: {int(price *(1 - discount / 100))}')

print("2. feladat: Filmkód generálása")
def get_code(n:str, y:int) -> str:
    title =  n[0:4:1].upper() + str(y)[2:] + '-'
    return title + str(len(title))

try:
    name = input("Add meg a film cimet: ")
    year = int(input('Add meg a megjelenesi evet: '))
    if len(name) == 0 or year < 1888 or year > 2026:
        print("Helytelen adatot adott meg!")
    else:
        print(f'A film kodja: {get_code(name, year)}')
except:
    print("Érvénytelen számot adott meg!")

print('3. feladat: Filmadatbázis')
class Data:
    def __init__(self, line: str) -> None:
        self.row = line.strip().split('#')
        self.name = self.row[0]
        self.genre = self.row[1]
        self.year = int(self.row[2])
        self.raiting = float(self.row[3].replace(',', '.'))
        self.duration = int(self.row[4])

with open('filmek.txt', 'r', encoding='UTF-8') as f:
    raw = f.readlines()

content: list[Data] = []
for i in range(1, len(raw), 1):
    content.append(Data(raw[i]))

def get_lenght(content: list) -> int:
    return len(content)

print(f'A filmek szama: {get_lenght(content)}')

i = 0
found = False
while i < len(content) and not found:
    if content[i].year < 1990:
        found = True
    i += 1

if found:
    print("Van 1990 előtti film a listában.")
else:
    print("Nincs 1990 előtti film a listában.")

def get_best_raiting(content: list) -> str:
    best = 0.0
    result = ''
    for line in content:
        if line.raiting > best:
            best = line.raiting
            result = f'{line.name}, ertekelese: {line.raiting}'
    return result

print(f'A legjobb ertekelesu film: {get_best_raiting(content)}')

def get_duration_avg(content: list) -> float:
    durations = []
    result = 0.0
    for i in content:
        durations.append(i.duration)
     
    for n in durations:
        result += n

    return result / len(durations)

print(f"A filmek atlagos hossza: {get_duration_avg(content):.1f} perc.")

def get_scifi(content: list) -> list:
    result_list = []
    for line in content:
        if line.genre == 'sci-fi':
            result_list.append(f"{line.name}\t{line.year}\n")
    return result_list

with open('sci_fi.txt', 'w', encoding='utf-8') as new_f:
    new_f.write("Cím\tÉv\n")
    new_f.writelines(get_scifi(content))