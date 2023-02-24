import json

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
    info = json.load(f)

char = []
for act in info["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in char:
                char.append(action["character"])

new_info = {}
for character in char:
    c = 0
    for act in info["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                if action["character"] == character:
                    c += 1
    new_info[character] = c

lines_max = 0
char_name = None
for character in new_info:
    if new_info[character] >= lines_max:
        lines_max = new_info[character]
        char_name = character
print(char_name)