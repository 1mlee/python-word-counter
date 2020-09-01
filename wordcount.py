import time
listchar = [0] * 10000
start = int(round(time.time() * 1000))
with open ("newtext.txt", "r") as file:
    data = file.read().replace('\n', '')
    for char in data:
        indexlist = ord(char)
        listchar[indexlist] = listchar[indexlist] + 1
    for i in range(len(listchar)):
        if(listchar[i] != 0):
            print(chr(i) + "-" + str(listchar[i]))
    maximnumber = max(listchar)
    newlist = listchar
    indexs = listchar.index(maximnumber)
    print("Чаще всего встречался символ - '" + chr(indexs) + "'")
    del listchar[indexs]
    maximnumber = max(listchar)
    indexs = listchar.index(maximnumber)
    print("После него чаще всего встречался символ - '" + chr(indexs) + "'")
    print("Символы по частоте:")
    for i in range(len(listchar)):
        maximnumber = max(listchar)
        if maximnumber != 0:
            newlist = listchar
            indexs = listchar.index(maximnumber)
            print(str(i + 1) + " - " + chr(indexs) + "(" + str(maximnumber) + ")")
            del listchar[indexs]
    print("Всего символов в этом документе - " + str(len(data)))
    end = int(round(time.time() * 1000))
    print("Время выполнения программы заняло : " + str(end - start) + "ms")