import csv

with open('3.csv', 'w', encoding='utf-8') as d:
    fieldnames = ["Id", "Images", "Title", "Description", "Price"]
    writer = csv.DictWriter(d, fieldnames=fieldnames)
    #writer.writeheader()
    with open('stage3_test.csv', 'r',encoding='utf-8' ) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            del row['Images']
            del row['Description']
            writer.writerow(row)