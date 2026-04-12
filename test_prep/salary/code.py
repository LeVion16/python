class salary:
    def __init__(self, line:str) -> None:
        self.row = line.strip().split(';')
        self.name = self.row[0]
        self.gender = self.row[1]
        self.section = self.row[2]
        self.entrance = self.row[3]
        self.salary = int(self.row[4])

with open('./berek.csv', 'r', encoding='utf-8') as f:
    raw = f.readlines()

content: list[salary] = []
for i in range(1, len(raw), 1):
    content.append(salary(raw[i]))

n = input('Adj meg egy nevet: ')

def get_employes(content: list[salary], n: str) -> list:
    people = []
    for line in content:
        if n in line.name:
            people.append(line.name)
    return people

workers_list = get_employes(content, n)
print(workers_list)


def get_salary(content: list[salary], n: str):
    summa = 0
    for line in content:
        if n in line.name:
            summa += line.salary
    return summa

print(f'A {n} nevu dolgozok fizetese: {get_salary(content, n)}')