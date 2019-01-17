Project title
# Creating a bed file from LRG xml data
MSc BIOL68400 bioinformatics course group work


### Purpose
The python script in this repository was developed to convert a Locus Reference Genomic (LRG) data in xml format and output data in a bed format. A bed file format is more human friendly format and used widely in genomic tools. 


### Build Status
The work completed. No more development after the submission deadline on 18th January, 2019.

### Code Style
Standard.

### Features
This script simply pulls out chromosome, start and end positions from a LRG xml format file and creates a bed format file as an output. The LRG xml files are avaialbe to download from https://www.lrg-sequence.org/.

### Code Example
 ```python
python LRGParser.py {your_LRG_xml_file_name}
```
### Requirements
- Python == 3.7.0.
- pytest == 4.0.2.

This script was developed and tested using Python 3.7.0 and pytest 4.0.2. It has been tested on Python 2.7.3 and pytest 4.0.2 and works. However, using any other version may cause errors or faulty results. 

### Installation
Download the script LRGParser.py to your local computer which is equipped with the requirements. 


### API Reference
Not available.

### Tests
The script was tested using pytest 4.0.2. Please refer the script: 
```python 
test_LRGParser.py
```


### How to use
 ```python
python LRGParser.py {your_LRG_xml_file_name, usually "LRG_{X}.xml"}
```
xml files to use have to be in the same directory or specify an absolute path.

Then the output file (usually as LRG_{X}.bed) looks like this:
```python
Chromosome Number       Start   End     Exon Number
Chr17   48279000        48278772        Ex 1
Chr17   48277308        48277114        Ex 2
Chr17   48276951        48276917        Ex 3
Chr17   48276814        48276779        Ex 4
Chr17   48276688        48276587        Ex 5
Chr17   48275865        48275794        Ex 6
Chr17   48275566        48275522        Ex 7
Chr17   48275363        48275310        Ex 8
Chr17   48275146        48275093        Ex 9
Chr17   48274594        48274541        Ex 10
...
```

### Contribution
- Seemu Ali and Seiko Makino equally contributed development of this work.

### Acknowledgements
- The University of Manchester BIOL68400 Programming Module, Prof Andy Brass for the course work and helping us out to write codes.

### License
 - Copyright (C) 2018 University of Manchester and NHS STP 
 - Authors: Seemu Ali (github.com/SeemuAli) & Seiko Makino (github.com/seikom)