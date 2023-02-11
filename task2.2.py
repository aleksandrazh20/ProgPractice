import csv

with open('2.csv', 'w', encoding = 'utf-8') as d:
    writer = csv.writer(d)
    with open('stage3_test.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[4] == 'Price':
                pass
            elif 10000 < float(row[4]) < 50000:
                writer.writerow(row)