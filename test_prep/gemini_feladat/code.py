# 1.Feladat--- 
class Data:
    def __init__(self, line: str) -> None:
        self.row = line.strip().split(';')
        self.name = self.row[0]
        self.gender = self.row[1]
        self.team = self.row[2]
        self.min = int(self.row[3])
        self.distance = int(self.row[4])

# 2.Feladat---
with open('bringasok.txt', 'r', encoding='UTF-8') as f:
    raw = f.readlines()

content: list[Data] = []
for i in range(1, len(raw), 1):
    content.append(Data(raw[i]))

'''
for o in content:
    print(f'{o.name}-{o.gender}-{o.team}-{o.min}-{o.distance}')
'''

# 3.Feladat---
def get_all_competitor(content: list[Data]) -> int:
    return len(content)

print(f'3. feladat-> {get_all_competitor(content)}')

# 4.Feladat---
def get_avg_time(content: list[Data]) -> float:
    time = []
    for line in content:
        time.append(line.min)
    
    return sum(time) / len(time)

print(f'4. feladat-> {get_avg_time(content)}')

# 5.Feladat---
def get_details(content: list[Data], team: str) -> list:
    details = []
    for i in content:
        if team == i.team:
            details.append(f'{i.name}-{i.min}-{i.gender}-{i.distance}')
    return details

t = input('Adj meg egy csapatot: ')

details = get_details(content, t)
if len(details) > 0:
    print(f'5. feladat -> {details}')
else:
    print('Ez a csapat nem indult.')

'''
# 6.Feladat---
def get_fastest_competior(content: list[Data]) -> list:
    fastest = []
    start = 1000
    for i in content:
        if i.min < start:
            start = f'{i.name}-{i.team}-{i.min}'
    return fastest

print(f'6. feladat -> {get_fastest_competior(content)}')
'''
# 7.Feladat---
def get_competitior_by_gender(conent: list[Data]) -> list:
    ferfiak =  0
    nok =  0
    for i in conent:
        if i.gender == 'no':
            nok += 1
        else :
            ferfiak += 1
    final_list = []
    final_list.append(ferfiak)
    final_list.append(nok)
    return final_list

get_competitior_by_gender(content)
with open('statisztika.txt', 'w', encoding='UTF-8') as f:
    f.write(f"Ferfiak: {get_competitior_by_gender(content)[0]}\n")
    f.write(f"Nok: {get_competitior_by_gender(content)[1]}\n")