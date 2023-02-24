import json

data1 = []
with open('wikidata_1000.json', 'r', encoding='utf-8') as f:
    for line in f:
        data1.append(json.loads(line))

data2 = {}
for line in data1:
    if "description" in line:
        data2[line["label"]["value"]] = line["description"]["value"]
    else:
        data2[line["label"]["value"]] = "None"

with open('1.json', 'w') as d:
    json.dump(data2, d, ensure_ascii=False, indent=4)