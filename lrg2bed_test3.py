
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

#first argument listed after script is saved as file_name  
file_name = sys.argv[1] 


# parse file_name to python as 'root'
tree=ET.parse(file_name)
root = tree.getroot()

#a loop to find all transcripts and genomic builds in file to only pull out chromosome information for 37 build
for mapping in root.findall(".//updatable_annotation/annotation_set/mapping"):
    if mapping.get('coord_system').startswith("GRCh37"): 
        Chrom_number = int(mapping.get('other_name')) #define variable as an integer value as oppose to string
        Chrom_start = int(mapping.get('other_start')) #define variable as an integer value as oppose to string
        Chrom_end = int(mapping.get('other_end'))     #define variable as an integer value as oppose to string
        Strand = mapping.find('mapping_span').get('strand')
        print(Chrom_number, Chrom_start, Chrom_end, Strand)



# defining list sections before appending exon start and end positions from loop 
label=[]
start=[]
end=[]
#pos=[]

#a loop to find all exons and append the label start and end of the exon coordinates then calculate position in GRch37 build
# an if function added to ensure correct loop and calculation is ran depending if strands are forward or reverse

if Strand == '1':
    for exon in root.findall(".//fixed_annotation/transcript/exon"):
        label.append(exon.get('label'))
        coordinates = exon.find('coordinates')
        LRG_start = int(coordinates.get('start')) #define variable as an integer value as oppose to string
        LRG_end = int(coordinates.get('end')) #define variable as an integer value as oppose to string
        Exon_start = Chrom_start + LRG_start - 1 #calculates Exon start position in GRCH37 forward strand
        Exon_end = Chrom_start + LRG_end -1 #calculates Exon start position in GRCH37 forward strand 
        start.append(Exon_start)
        end.append(Exon_end)
        print('Forward strand')

elif Strand == '-1':
    for exon in root.findall(".//fixed_annotation/transcript/exon"):
        label.append(exon.get('label'))
        coordinates = exon.find('coordinates')
        LRG_start = int(coordinates.get('start')) #define variable as an integer value as oppose to string
        LRG_end = int(coordinates.get('end')) #define variable as an integer value as oppose to string
        Exon_start = Chrom_end - LRG_start + 1 #calculates Exon start position in GRCH37 forward strand
        Exon_end = Chrom_end - LRG_end + 1 #calculates Exon start position in GRCH37 forward strand 
        start.append(Exon_start)
        end.append(Exon_end)
        print ('Reverse strand')
else:
    print ('Strand not defined as forward or reverse')
    quit() 

#saves output into bedfile format 
bedfilename = "{}.bed".format(file_name.rstrip('.xml')) #bed file saved in accordance to initial xml filename 

outfile = open(bedfilename,"w")
outfile.write("Chromosome Number\tStart\tEnd\tExon Number\n")
for i in range(len(start)):
    outfile.write("Chr{}\t{}\t{}\tEx {}\n".format(Chrom_number,start[i],end[i],label[i]))
outfile.close()




