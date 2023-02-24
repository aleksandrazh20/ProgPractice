import json

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
    info = json.load(f)

result = []
for act in info["acts"]:
    for scene in act["scenes"]:
        characters = []
        for action in scene["action"]:
            if action["character"] not in characters:
                characters.append(action["character"])
        result.append(characters)

with open('2.json', 'w') as d:
    d.write(json.dumps(result,ensure_ascii=False, indent=4))