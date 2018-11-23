# running this python script from shell with a LRG.xml file as an argument
import sys
import xml.etree.ElementTree as ET

# 
file_name = sys.argv[1]

# parse file_name to python as 'root'
tree=ET.parse(file_name)
root = tree.getroot()

# pull out exon, start and end positions from 'exon' within 'transcript'
for exon in root.findall(".//fixed_annotation/transcript/exon"):
    label = exon.get('label')
    coordinates = exon.find('coordinates')
    start = coordinates.get('start')
    end = coordinates.get('end')
    print(label,start,end)

