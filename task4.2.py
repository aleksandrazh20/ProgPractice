import xml.etree.ElementTree as et

tree = et.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('plur.txt', 'w', encoding='utf-8') as f:
    for tokens in root.iter('tokens'):
        for token in tokens.findall('token'):
            nouns = []
            for g in token.iter('g'):
                nouns.append(g.attrib['v'])
            if 'NOUN' in nouns and 'plur' in nouns:
                f.write(token.attrib['text']+'\n')


