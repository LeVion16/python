# 1.Feladata
output = ['név*e-mail-cím*jelszó*születési dátum'.replace('*',';')]
with open('./user.txt','w',encoding='UTF-8') as f:
    for line in output:
        print(line, file=f)

# 2.Feladat (a)
path = './orvosi_nobeldijak.csv'

header = list()
with open(path,"r",encoding='UTF-8') as raw:
    file = raw.readlines()
    
header = file[0].strip().split(";")

content = list()
for i in range(1, len(file), 1):
    line = file[i].strip().split(";")
    d = dict()
    d['Év'] = int(line[0])
    d['Név'] = line[1]
    d['SzületésHalálozás'] = line[2]
    d['Országkód'] = line[3]
    content.append(d)
    
# 2.Feladat (b)
def get_summa(array: list) -> int:
    summa = 0
    for line in array:
        if line['SzületésHalálozás'].endswith('-'):
            continue
        else:
            summa += 1
    return summa

print(f'Ma már nem élő díjjazottak száma: {get_summa(content)}')

# 2.Feladat (c) start stop step
def get_biggest_year(array: list) -> int:
    years = list()
    for line in array:
        years.append(line['SzületésHalálozás'][5::1])
    return years

print(f'Az utolsó év: {get_biggest_year(content)}')
        
# 2.Feladat (d)
def get_county(array:list, input_code) -> str:
    result = []
    for line in array:
        if input_code in line["Országkód"]:
            result.append(f"{line["Év"]}|{line["Név"]}|{line["SzületésHalálozás"]}|{line["Országkód"]}")
    return result
 
result_list = []
result_list = get_county(content, 'USA')
count = 0
for line in result_list:
    count += 1
    
if count == 1:
    print(result_list)
else:
    print(f'A megadott országból {count} fő volt díjjazott')