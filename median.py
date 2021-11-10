import csv

with open("hw.csv",newline="") as g:
    reader=csv.reader(g)
    filedata = list(reader)

filedata.pop(0)

newData = []

for i in range(len(filedata)) :
    num = filedata[i][2]
    newData.append(float(num))

n = len(newData)

if n%2 == 0 :
    m1 = newData[n//2]   
    m2 = newData[n//2 - 1]
    meidan = (m1 + m2)/2
else :
    meidan = newData[n//2]

print("Median is ",meidan)

