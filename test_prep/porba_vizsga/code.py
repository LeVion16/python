# Task 1.
def get_number(n1, n2) -> int:
    if n1 == n2:
        return 1
    elif n1 > n2:
        return 2
    else:
        return 3
    
num1 = int(input('Kerem az elso szamot: '))
num2 = int(input('Kerem a masodik szamot: '))

decider = get_number(num1, num2)
if decider == 1:
    print('A ket szam egyenlo')
elif decider == 2:
    print(f'A nagyobb szam {num1}, a kisebb {num2}')
elif decider == 3:
    print(f'A nagyobb szam {num2}, a kisebb {num1}')

# Task 2.
def get_year(y1, y2):
    result_list  = list()
    for y in range(y1, y2, 1):
        if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
            result_list.append(y)
    return result_list

year1 = int(input('Kerem az egyik evszamot: '))
year2 = int(input('Kerem az egyik evszamot: '))

decider2 = get_year(year1, year2)
if len(decider2) > 0:
    print(decider2)
else:
    print('Nincs szokoev a megadott tartomanyban.')

# Task 3.1.
class Data:
    def __init__(self, line:str) -> None:
        self.row = line.strip().split(';')
        self.name = self.row[0]
        self.town = self.row[1]
        self.country = self.row[2]
        self.height = float(self.row[3].replace(',', '.'))
        self.floor = int(self.row[4])
        self.built = int(self.row[5])

with open('./legmagasabb.txt', 'r', encoding='UTF-8') as f:
    raw = f.readlines()

content: list[Data] = []
for i in range(1, len(raw), 1):
    content.append(Data(raw[i]))

# Task 3.2.
def get_all_building(content: list) -> int:
    return len(content)

print(f'Epuletek szama: {get_all_building(content)}db.')

# Task 3.3.
def get_floor_summa(content: list) -> int:
    summa = 0
    for i in content:
        summa += i.floor
    return summa

print(f'Emeletek osszege: {get_floor_summa(content)}')

# Task 3.4
def get_details(content: list):
    # Feltételezzük, hogy az első a legmagasabb
    highest_building = content[0]

    # Végigmegyünk a listán
    for building in content:
        # Ha a mostani épület magasabb, mint az eddigi legmagasabb
        if building.height > highest_building.height:
            highest_building = building # Ő lesz az új csúcstartó
    
    details = list()
    details.append(f'{highest_building.name}-{highest_building.town}-{highest_building.country}-{highest_building.height}-{highest_building.floor}-{highest_building.built}')
    return details

header = ['nev:varos:orszag:magassag:emelet:epult']
details_list = get_details(content)

with open('./legmasabb2.txt', 'w', encoding='UTF-8') as f:
    file = f.writelines(header)
    # Végigmegyünk a részleteket tartalmazó listán és kiírjuk a sorokat
    for row in details_list:
        f.write(row + '\n') # Új sor karaktert teszünk a végére, hogy ne folyjon össze

# Task 3.5.
def get_italy(content: list) -> bool:
    i = 0
    # Addig megyünk, amíg bent vagyunk a listában ÉS a jelenlegi épület NEM olasz
    while i < len(content) and content[i].country != 'Olaszország':
        i += 1

    # Ha a ciklus azért állt le, mert az i kisebb maradt, mint a lista hossza,
    # az azt jelenti, hogy találtunk olasz épületet (megszakadt a feltétel).
    if i < len(content):
        return True
    else:
        return False
    
if get_italy(content):
    print('Van olasz epulet az adatok kozott!')
else:
    print('Nincs olasz epulet az adatok kozott!')