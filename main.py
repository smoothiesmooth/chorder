import time
import os

tuningList = {
    "Standard" : ["E", "B", "G", "D", "A", "E"],
    "Drop D" : ["E", "B", "G", "D", "A", "D"]
} 

with open("song.scrd", 'r') as f:
    dataList = f.read().split('|')
    dataList[1] = dataList[1].split(" ")

currentTuning = tuningList[dataList[0]]
chordList = dataList[1]

rows, columns = os.popen('stty size', 'r').read().split()

tabString1 = currentTuning[0] + " " + "-"*len(chordList)*2
tabString2 = currentTuning[1] + " " + "-"*len(chordList)*2
tabString3 = currentTuning[2] + " " + "-"*len(chordList)*2
tabString4 = currentTuning[3] + " " + "-"*len(chordList)*2
tabString5 = currentTuning[4] + " " + "-"*len(chordList)*2
tabString6 = currentTuning[5] + " " + "-"*len(chordList)*2

tab = ''''''

tabList = [tabString1, tabString2, tabString3, tabString4, tabString5, tabString6]

def inject(where, what, index): # Inject chord to string
    return where[:index] + what + where[index+1:]

def makeTab(tl, cl): # Complete tab
    global tab
    index = 3
    iterNum = 0
    for j in cl:
        tl[0] = inject(tl[0], cl[iterNum][0], index)
        tl[1] = inject(tl[1], cl[iterNum][1], index)
        tl[2] = inject(tl[2], cl[iterNum][2], index)
        tl[3] = inject(tl[3], cl[iterNum][3], index)
        tl[4] = inject(tl[4], cl[iterNum][4], index)
        tl[5] = inject(tl[5], cl[iterNum][5], index)

        iterNum += 1

        index += 2

    for item in tabList:
        tab+=item + '\n'

makeTab(tabList, chordList)

if __name__ == "__main__":

    print("Добро пожаловать в генератор табуляций!")
    print("Создатель: @whitepear\n")

    time.sleep(1)

    os.system("cls")

    print(tab)    

    if input("Для выхода нажмите Enter\n"):
        raise SystemExit

