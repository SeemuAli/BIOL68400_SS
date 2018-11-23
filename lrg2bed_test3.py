
"""
Usage: lrg2bed_test2.py LRG_?.XML 

This script extracts exon start and end positions from LRG XML files

"""

# running this python script from shell with a LRG.xml file as an argument
import sys
import xml.etree.ElementTree as ET

#first argument saved as file_name  
file_name = sys.argv[1]

# parse file_name to python as 'root'
tree=ET.parse(file_name)
root = tree.getroot()

# pull out exon, start and end positions from 'exon' within 'transcript'
label=[]
start=[]
end=[]
pos=[]

#a loop to find all exons and append the label start and end of the exon coordinates
for exon in root.findall(".//fixed_annotation/transcript/exon"):
    label.append(exon.get('label'))
    coordinates = exon.find('coordinates')
    start.append(coordinates.get('start'))
    end.append(coordinates.get('end'))
#  print(label, "\t", start,"\t",end)

for i in range(len(start)):
    print(str(label[i]) + "\t "+ str(start[i]) + "\t" + str(end[i]) +"\n")

#print(pos)

outfile = open("test.bed","w")
outfile.write("Hello")
for i in range(len(start)):
    print(str(label[i]) + "\t "+ str(start[i]) + "\t" + str(end[i]) +"\n",file=outfile)
outfile.close()



#    print(i)
#labelpos=label[i]
#startpos=start[i]
#print(startpos)
#file.write(startpos,labelpos)
