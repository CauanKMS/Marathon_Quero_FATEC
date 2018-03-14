multiplos = [2, 3, 4, 5]

multUser = []

breakParam = False

primMultUser = int(input())

while breakParam == False:
    Li = int(input())

    if Li <= 1 or Li > 100:
        breakParam = True
    else:
        multUser.append(Li)


qtdMulti_2 = 0
qtdMulti_3 = 0
qtdMulti_4 = 0
qtdMulti_5 = 0

if primMultUser % multiplos[0] == 0:
    qtdMulti_2 += 1

if primMultUser % multiplos[1] == 0:
    qtdMulti_3 += 1

if primMultUser % multiplos[2] == 0:
    qtdMulti_4 += 1

if primMultUser % multiplos[3] == 0:
    qtdMulti_5 += 1

for i in multUser:
    if i % multiplos[0] == 0:
        qtdMulti_2 += 1

    if i % multiplos[1] == 0:
        qtdMulti_3 += 1

    if i % multiplos[2] == 0:
        qtdMulti_4 += 1

    if i % multiplos[3] == 0:
        qtdMulti_5 += 1

print(str(qtdMulti_2) + " Multiplo(s) de 2")
print(str(qtdMulti_3) + " Multiplo(s) de 3")
print(str(qtdMulti_4) + " Multiplo(s) de 4")
print(str(qtdMulti_5) + " Multiplo(s) de 5")