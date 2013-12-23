import csv, os

for filename in os.listdir("results"):
    if not filename.startswith(".DS"):
        reader = csv.reader(open(os.path.join("results",filename), 'r'), delimiter=',')
        newFile = filename.replace(".","_")
        newFile = newFile + "resultUnique.csv"
        writer=csv.writer(open(os.path.join("results",newFile), 'w'), delimiter=',')
        rsslinks = set()
        for row in reader:
            if row[1] not in rsslinks:
                writer.writerow(row)
                rsslinks.add( row[1] )