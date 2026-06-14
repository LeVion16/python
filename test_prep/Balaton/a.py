# Task 1.
class Data:
    def __init__(self, line: str) -> None:
        self.row = line.strip().split(';')
        self.competitor = self.row[0]
        self.number = int(self.row[1])
        self.category = self.row[2]
        self.time = int(self.row[3].replace(':', ''))
        self.distant = int(self.row[4])

with open('./ub2017.csv', 'r', encoding='UTF-8') as f:
    raw = f.readlines()

content: list[Data] = []
for i in range(1, len(raw), 1):
    content.append(Data(raw[i]))

# Task 2.
def get_females(content: list) -> int:
    summa = 0
    for i in content:
        if i.category == 'Noi' and i.distant == 100:
            summa =+ 1
    return summa

print(f'A teljes tavot {get_females(content)} noi sportolo teljesitette.')

#Task 3.
def get_details(content: list, n) -> list:
    details = list()
    for i in content:
         if i.number == n:
             details.append(f'Neve: {i.competitor}, versenyideje: {i.time}')
             break
    return details

number =  int(input('Adja  meg a rajtszamot: '))
print(f'A {number} - rajtszamu versenyzo: {get_details(content, number)}')