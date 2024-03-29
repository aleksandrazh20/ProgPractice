import xml.etree.ElementTree as et

tree = et.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('sentences.txt', 'w', encoding='utf-8') as f:
    for source in root.iter('source'):
        f.write(source.text+"\n")