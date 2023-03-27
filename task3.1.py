import json


data = {}
for line in open('wikidata_1000.json', 'r', encoding='utf-8'):
    line = json.loads(line)
    key = line["label"]['value']
    try:
        value = line["description"]['value']
    except:
        value = 'None'
    data[key] = value

with open('res1.json', 'w') as f:
    json.dump(data, f, sort_keys=False, ensure_ascii=False, indent=4)


