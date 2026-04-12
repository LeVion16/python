class RadioLog:
    def __init__(self, line: str) -> None:
        self.row = line.strip().split(';')
        self.hour = int(self.row[0])
        self.min = int(self.row[1])
        self.AdasDb = int(self.row[2])
        self.name = self.row[3]

    def convert_mins(self) -> int:
        return self.hour * 60 + self.min

path = './cb.csv'
with open(path, 'r', encoding='UTF-8') as f:
    raw = f.readlines()

content: list[RadioLog] = []
for i in range(1, len(raw), 1):
    content.append(RadioLog(raw[i]))

""" 
for o in content:
    print(f'{o.hour}-{o.min}-{o.AdasDb}-{o.name}')
 """

#---
def get_post(content: list[RadioLog]) -> int:
    '''This function gets all the posts from the source'''
    return len(content)
    
print(f'Osszesen {get_post(content)} bejegyzes talalhato a forrasallomanyban. ')

print()
#---
def get_4_calls(content: list[RadioLog]) -> bool:
    '''Gets the pilot that started 4 calls under one mins'''
    i = 0
    while i < len(content) and i < content[i].AdasDb != 4:
        i += 1
    return i < len(content)

get_4_calls(content)
if get_4_calls == True: print('Volt 4 dast indito sofor.')
else: print('Nem volt 4 adast indito sofor.')

print()
#---
n = input('Adjon meg egy nevet: ')

def get_pilot_by_name(content: list[RadioLog], n: str) -> int:
    summa = 0
    for i in content:
        if i.name == n:
            summa =+ i.AdasDb
    return summa

adas = get_pilot_by_name(content, n)
if adas > 0:
    print(f'{n} {adas} - adast inditott.')
else:
    print('nincsen ilyen nev vagy nem inditott adast.')

output = ['perc;AdasDb;Nev']
for line in content:
    output.append(f'{line.convert_mins};{line.name};{line.AdasDb}')

with open('cb2.txt','w',encoding='utf-8') as f:
    for line in output:
        print(line, file=f)