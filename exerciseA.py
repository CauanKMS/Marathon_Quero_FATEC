bits = [2, 3, 4, 5]

bitUser = []

breakParam = False

while breakParam == False:
    bitU = int(input("V: \n"))

    if bitU <= 0 or bitU > 10000:
        breakParam = True
    else:
        bitUser.append(bitU)


bitGive = [0, 0, 0, 0]
testN = 0

for i in bitUser:
    while i != 0:

        if i % bits[0] == 0:
            bitGive[0] += 1
            i -= bits[0]

        elif i % bits[1] == 0:
            bitGive[1] += 1
            i -= bits[1]

        elif i % bits[2] == 0:
            bitGive[2] += 1
            i -= bits[2]

        elif i % bits[3] == 0:
            bitGive[3] += 1
            i -= bits[3]
    testN += 1
    print("Teste " + str(testN) + "\n" + str(bitGive[0]) + " " + str(bitGive[1]) + " " + str(bitGive[2]) + " " + str(bitGive[3]))