def recensement():
    aglomeration_totale=0
    k=0
    import csv
    table=[]
    with open("donnees_2008.csv",newline="") as csvfile:
        csvfile.readline()
        reader=csv.reader(csvfile,delimiter=",")
        for row in reader:
            table.append(row)
    table2=[]
    with open("donnees_2016.csv",newline="") as csvfile:
        csvfile.readline()
        reader=csv.reader(csvfile,delimiter=",")
        for row in reader:
            table.append(row)
    table3=[]
    with open("donnees_2021.csv",newline="") as csvfile:
        csvfile.readline()
        reader=csv.reader(csvfile,delimiter=",")
        for row in reader:
            table.append(row)
    for i in range(len(table)):
        if int(table[i][0])==89:
            aglomeration_totale+=int(table[i][6])
            print(aglomeration_totale)
    return table



print(recensement())
