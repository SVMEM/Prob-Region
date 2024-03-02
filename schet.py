import csv
usr = []
dic = {}
with open("nicks.csv", 'r') as fin:
    rid = csv.reader(fin)
    for row in rid:
        dic[row[0]] = row[1]

with open("ribyata.csv", 'r') as fin:
    rid = csv.reader(fin)
    for row in rid:
        s = 0
        usi = []
        usi.append(row[0])
        usi.append(row[1])
        usi.append(dic[row[0]])
        if row[2] == '3':
            s += 2
        if row[3] == '2':
            s += 2
        if row[4] == '3':
            s += 2
        if row[5] == '1':
            s += 2
        if row[6] == '3':
            s += 2
        if row[7] == '23':
            s += 3
        if row[8] == '124':
            s += 3
        if row[9] == '134':
            s += 3
        if row[10] == '2':
            s += 3
        if row[11] == '134':
            s += 3
        s += 3
        if row[13] == '1000':
            s += 3
        if row[14] == '0':
            s += 3
        if row[15] == '1331':
            s += 3
        if row[16] == '350':
            s += 3
        usi.append(s)
        usr.append(usi)

with open('uu.csv', 'w') as fin:
    writ = csv.writer(fin)
    for i in usr:
        writ.writerow(i)
