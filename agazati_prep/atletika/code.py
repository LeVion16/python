import random as rr
import string

class Data:
    def __init__(self, line: str) -> None:
        self.row = line.strip().split('&')
        self.name = self.row[0]
        self.country = self.row[1]
        self.competition_num = self.row[2]
        self.result =  float(self.row[3].replace(',', '.'))
        self.medal = self.row[4]

with open('atletak.txt', 'r', encoding='UTF-8') as f:
    raw = f.readlines()

content: list[Data] = []
for i in range(1, len(raw), 1):
    content.append(Data(raw[i]))

print('1. feladat: Futóverseny-értékelés')
name = input('Add meg a versenyző nevét: ')
distante = int(input('Add meg a futott táv hosszát (km): '))
duration = float(input('Add meg a teljesített időt (óra): '))
avg = distante / duration
print(f'{name} atlagsebessege: {avg:.2f} km/h')
classification = ''
if avg < 6:
    classification = 'gyaloglas'
elif avg < 12:
    classification = 'kocogas'
elif avg > 12:
    classification = 'futas'
print(f'Besorolas: {classification}')

print('2. feladat: Versenyző-azonosító generálása')
n = input('Add meg a versenyző nevét: ')
num = int(input('Add meg a rajtszámot: '))

def generate_id(content: list, n: str, num: int) -> str:
    result = str(ord(n[0]) - 64) + str(num) + '-'
    # 2. rész: 2 nagybetű és 2 kisbetű generálása
    nagybetuk = rr.choices(string.ascii_uppercase, k=2)
    kisbetuk = rr.choices(string.ascii_lowercase, k=2) 
    # Összeöntjük és összekeverjük őket
    karakterek = nagybetuk + kisbetuk
    rr.shuffle(karakterek)
    # Hozzáadjuk a véletlen karaktereket is a result-hoz
    result += "".join(karakterek) 
    return result

print(generate_id(content, n, num))

print('3. feladat: Atlétikai adatbázis')
def get_athletes(content: list) -> int:
    return len(content)

print(f'Az atléták száma: {get_athletes(content)}')

def get_Nederland(content: list) -> bool:
    for i in content:
            if i.country + 'Hollandia':
                return True
            return False
    
nederland = get_Nederland(content)
if nederland:
    print('Található a versenyzők között holland.')
else:
    print('Nem található a versenyzők között holland.')

def get_weakest(content: list) -> str:
    n = ''
    t = 0.0
    for line in content:
        if line.competition_num == "100 m":
            if line.result > t:
                n = line.name
                t = line.result
    return f'{n}, ido: {t} mp'

print(f'A leggyengébb 100 m-es futó: {get_weakest(content)}')

def avg_result(content: list) -> int:
    results = []
    for i in content:
        results.append(i.result)

    avg = 0
    for n in results:
        avg += n
    
    return avg / len(results)

print(f'Az atléták átlagos eredménye: {avg_result(content):.2f} mp')

def get_gold(content: list):
    medalists = []
    for i in content:
        if i.medal == 'arany':
            line = f"{i.name};{i.competition_num}\n"
            medalists.append(line)
    return medalists

with open('aranyermesek.txt', 'w', encoding='utf-8') as new_f:
    new_f.writelines('Nev;Szam')
    new_f.writelines(get_gold(content))