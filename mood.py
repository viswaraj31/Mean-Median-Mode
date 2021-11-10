import csv
from collections import Counter

with open("hw.csv",newline="") as g:
    reader=csv.reader(g)
    filedata = list(reader)

filedata.pop(0)

newData = []

for i in range(len(filedata)) :
    num = filedata[i][2]
    newData.append(float(num))

data = Counter(newData)

modeRange = {
    "90-100" : 0 ,
    "100-110" : 0 ,
    "110-120" : 0 ,
    "120-130" : 0 ,
    "130-140" : 0 ,
    "140-150" : 0 ,
    "150-160" : 0 ,
    "160-170" : 0 ,
    "170-180" : 0 
}

for weight,occ in data.items() : 
    if 90<weight<100 :
        modeRange["90-100"] += occ
    elif 100<weight<110 :
        modeRange["100-110"] += occ
    elif 110<weight<120 :
        modeRange["110-120"] += occ
    elif 120<weight<130 :
        modeRange["120-130"] += occ
    elif 130<weight<140 :
        modeRange["130-140"] += occ
    elif 140<weight<150 :
        modeRange["140-150"] += occ
    elif 150<weight<160 :
        modeRange["150-160"] += occ
    elif 160<weight<170 :
        modeRange["160-170"] += occ
    elif 170<weight<180 :
        modeRange["170-180"] += occ

weiRange,modeocc = 0,0

for range,occ in modeRange.items() :
    if occ > modeocc :
        weiRange = [int(range.split("-")[0]),int(range.split("-")[1])]
        modeocc = occ

mode = float((weiRange[0]+weiRange[1])/2)

print(mode)