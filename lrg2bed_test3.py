
"""
Usage: lrg2bed_test2.py LRG_?.XML 

This script extracts exon start and end positions from LRG XML files

"""

#running this python script from shell with a LRG.xml file as an argument

import sys
import xml.etree.ElementTree as ET

#checking a file is included in argument for script to run 
if len (sys.argv) < 2:

	print ('please add LRG file for script to run')
	quit()

#first argument saved as file_name  
file_name = sys.argv[1] 


# parse file_name to python as 'root'
tree=ET.parse(file_name)
root = tree.getroot()

# defining list sections before appending exon, start and end positions from loop 
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



#a loop to find all exons and append the label start and end of the exon coordinates
#for exon in root.findall(".//updatable_annotation/mapping"):
    #label.append(exon.get('label'))
    #coordinates = exon.find('coordinates')
    #start.append(coordinates.get('start'))
    #end.append(coordinates.get('end'))


outfile = open("test.bed","w")
outfile.write("Exon\tStart\tEnd\n")
for i in range(len(start)):
    outfile.write("{}\t{}\t{}\n".format(label[i],start[i],end[i]))
outfile.close()




