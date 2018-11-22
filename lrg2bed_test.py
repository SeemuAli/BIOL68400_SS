import xml.etree.ElementTree as ET

# parse "LRG_1.xml" to python as 'root'
tree=ET.parse("LRG_1.xml")
root = tree.getroot()

# pull out exon, start and end positions from 'exon' within 'transcript'
for exon in root.findall(".//fixed_annotation/transcript/exon"):
    label = exon.get('label')
    coordinates = exon.find('coordinates')
    start = coordinates.get('start')
    end = coordinates.get('end')
    print(label,start,end)


