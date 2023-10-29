import mod1
import csv

lists = ["2023-10-01Sales.csv", "2023-10-01Sales.csv", "2023-09-01Sales.csv", "2023-09-01Sales.csv"]

for list in lists:
    with open("fileNames1.csv", "a", newline="") as file:
        fieldnames = ["filenames"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        #If file does not exist create header.
        if file.tell() == 0:
            writer.writeheader()        
        writer.writerow({"filenames": list})
                            
fileNamesList1 =set()
with open("fileNames1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        fileNamesList1.add(row["filenames"])
            
for fileNames in fileNamesList1:
    print(fileNames[0:]) 