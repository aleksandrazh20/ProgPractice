import collections
import json

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

chars = collections.defaultdict(list)
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                chars[action["character"]].append(line)

with open('5.2.json', 'w') as f:
    json.dump(chars, f, ensure_ascii=False, indent=4)