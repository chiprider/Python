
lines = []
csv = open("log.csv", "w")
with open('logdata.txt') as f:
    lines = f.readlines()

columns = []
for line in lines:
   columns = line.split()
   csv.write(columns[5].lstrip('"') + "," + columns[9] + "," + columns[8] + "," + '"' +  line.split(' "')[3].rstrip("\n") + "," + columns[10] + "\n")

csv.close()
    

