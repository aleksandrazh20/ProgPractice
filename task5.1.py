import collections
from collections import Counter
import json

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    info = json.load(f)
words = []
for act in info["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                for word in line.split(' '):
                    words.append(word)

most_common = Counter(words).most_common(20)
print(f"Most common:{most_common}")
least_common = collections.Counter(words).most_common()[-21::]
print(f"Least common: {least_common}")
