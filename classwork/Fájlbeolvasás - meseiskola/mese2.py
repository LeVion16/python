""" interface = open("./meseiskola.txt", "r", encoding="UTF-8")
raw_file = interface.readlines()
interface.close() """

with open("./meseiskola.txt", "r", encoding="UTF-8") as interface:
    raw_file = interface.readlines()

header = list()
content = list()

header = raw_file[0].replace('\n', '').split(";")
print((' |'.join(header)))

for i in range(1, len(raw_file), 1):
    content.append(raw_file[i].replace('\n', '').split(';'))
    
print(f"fejléc: \n{' | '.join(header)}")
print('Tartalom: ')
for line in content:
    print(' | '.join(line))
    
#Osztályok száma:
print(f"Az iskola osztályainak száma {len(content)} darab.")

#Nagy Judit osztályaának létszáma
def class_students(array: list, name: str) -> int:
    '''Adott ofö osztályának létszáma'''
    # Hol van N.J ?
    for line in array:
        if line[-1] == name:
            student = int(line[3]) + int(line[4])
    return student

print(f"Nagy Judit osztályának létszáma: {class_students(content, "Nagy Judit")} fő.")

#Hány osztálynak 4,0 a "tan" átlaga?
def get_4_average_class(array: list, average: str) -> int:
    '''Adott átlagú osztályok száma'''
    count = 0
    for line in array:
        if float(line[2].replace(',','.')) == float(average.replace(',','.')):
            count += 1
    return count

print(f"A 4,0 átlagú osztályok száma: {get_4_average_class(content, "4,0")}")

#Hány olyan ofö van akinek a neven "Nagy"-gyal kezdődik
def get_name(array: list, name: str) -> int:
    count = 0
    for line in array:
       #if line[-1][0:3:1] == name:
       #if line[-1].startswith(name):
        if line[-1].split(" ")[0] == name: #Itt minden olyan ember nevet keres amelyikben van "nagy" - szó.
            count += 1
    return count

print(f'Ofö-k száma, akiknek NAGY :) a nevük: {get_name(content, "Nagy")}')