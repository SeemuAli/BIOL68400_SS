import xml.etree.ElementTree as ET
tree=ET.parse("LRG_1.xml")
root = tree.getroot()

root[0][1].text
'2197'

>>> root[0][2].text
'NG_007400.1'

root[0][4][0].text

>>> root[0][4][0].text
'Osteogenesis Imperfecta Variant Database - COL1A1'


# extensible library for opening urls
# https://docs.python.org/2/library/urllib2.html
import urllib2
status_filename = urllib2.urlopen('url')


for transcript in root.findall('{./fixed_annotation/transcript}transcript'):
  coordinates= transcript.find('{./fixed_annotation/transcript}coordinates')
  print(coordinates.text)
  for start in transcript.findall('{./fixed_annotation/transcript/coordinates}start'):
    print(' |-->',start.text)


###
# this prints out 'start' positions in 'coordinates'
for coordinates in root.iter('coordinates'):
    #  print(coordinates.attrib)
  for start in coordinates.get('start'):
    start = coordinates.get('start')
    print(start)

# this print 'start' and 'end'
for coordinates in root.iter('coordinates'):
    #  print(coordinates.attrib)
    for start in coordinates.get('start'):
        start = coordinates.get('start')
    for end in coordinates.get('end'):
        end = coordinates.get('end')

    print(start,end)

# output
19718 20000
20133 20323
20620 20862
20992 22544


import xml.etree.ElementTree as ET
tree=ET.parse("LRG_1.xml")
root = tree.getroot()

for exon in root.findall(".//fixed_annotation/transcript/exon"):
  label = exon.get('label')
  coordinates = exon.find('coordinates')
  start = coordinates.get('start')
  end = coordinates.get('end')
  print(label,start,end)

##
for exon in root.iter('exon'):
    #    print(exon.attrib)
    print(coordinates.attrib)

for coordinates in root.iter('coordinates'):
    print(coordinates.attrib)
>>> coordinates.get('start')
'20992'


###
for exon in root.findall('./fixed_annotation/transcript/exon'): # 'transcript' only does not work. need 'exon'
  exon = exon.find('exon')
for exon in exon.find('./coordinates'):
  coordinates=exon.find('./coordinates')
  print(coordinates.text)
    for num in coordinates.find('./coordinates')
      print(num.txt)

coord=exon.get('coordinates')
coord.find('coord')
coord.text


