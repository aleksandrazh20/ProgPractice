import json

characters = list()
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for j in range(len(data['acts'])):
        for k in range(len(data['acts'][j]['scenes'])):
            chars = set()
            for l in range(len(data['acts'][j]['scenes'][k]['action'])):
                chars.add(data['acts'][j]['scenes'][k]['action'][l]['character'])
            chars = list(chars)
            characters.append(chars)
print(characters)
with open('2.json', 'w') as q:
    for i in characters:
        q.write(json.dumps(i))
        q.write("\n")


