import csv

with open('1.csv', 'w', encoding = 'utf-8') as d:
    fieldnames = ["Id", "Images", "Title", "Description", "Price"]
    writer = csv.DictWriter(d,fieldnames = fieldnames)
    writer.writeheader()
    with open('stage3_test.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter = ',')
        for row in reader:
            if len(row['Images'].split(',')) > 3:
                writer.writerow(row)


