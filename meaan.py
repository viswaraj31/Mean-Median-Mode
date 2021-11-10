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

sum = 0
for i in newData :
    sum += i

print("The mean is ",sum/n)
