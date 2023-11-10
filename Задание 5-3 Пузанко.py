mumiy = []
lampa = []
spisok = []
for i in range(int(input())):
    familia = (input())
    lampochka = (int(input()))
    if mumiy.count(familia) < 1:
        mumiy.append(familia),
        lampa.append(lampochka)
for i in range(len(mumiy)):
    structure = [mumiy[i], lampa[i]]
    print(structure)
    spisok.append(structure)
print(spisok)

for g in range(len(spisok) - 1):
    for k in range(len(spisok) - 1):
        if spisok[k] > spisok[k + 1]:
            spisok[k], spisok[k + 1] = spisok[k + 1], spisok[k]
print(spisok)