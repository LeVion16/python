text_path = "meseiskola.txt"

interface = open(text_path, "r", encoding="UTF-8")
#Itt dolgozunk a fájl tartalmával.
#interface.seek(16)
#print(f"Az interface tartalma:\n {interface}")
#print(f"A fájl tartalma2:\n {interface.readline()}, \ntípus:{type(interface.readline)}")
#interface.seek(0)
#print(f"A fájl tartalma1:\n {interface.read()}, \ntípus:{type(interface.read)}")
#interface.seek(0)
#print(f"A fájl tartalma3:\n {interface.read()}")
#interface.seek(0)
raw_content = interface.readlines()
interface.close()

print(interface) # Az interface itt már üres
#print(f"A fájl tartalma: \n{content}")
file_content = []
for row in raw_content:
    file_content.append(row.replace('\n', ''))

#print(file_content)

header = []
content_list = []
header = file_content[0].split(';')
for i in range(1, len(file_content), 1):
    content_list.append(file_content[i].split(';'))

print(header)
print(content_list)