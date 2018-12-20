Project title
# Creating a bed file from LRG xml data
MSc BIOL68400 bioinformatics course group work


### Purpose
The python script in this repository works to extract gene coordinates from a Locus Reference Genomic (LRG) data file (xml format) and output data in a bed format.

### Build Status
The work completed. No more development after the submission deadline on 18th January, 2019.

### Code Style
Standard.

### Screenshots

### Tech/Framework used

### Features
This script simply pulls out the exons, start and end positions from a LRG xml format file.

### Code Example
 ```python
lrg2bed_test3.py {your_LRG_xml_file_name}
```
### Requirements
This script was developed and tested using Python 3.7.0. It has been tested on Python 2.7.3, however using any other version may cause errors or faulty results. 

- Python == 3.7.0.
- pytest == X.X.

### Installation
Download the script lrg2bed_test3.py to your local computer which is equipped with the requirements. 


### API Reference
Not available.

### Tests

### How to use
 ```python
lrg2bed_test3.py {your_LRG_xml_file_name}
```
Then the output file looks like this:
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
- University of Manchester BIOL68400 Programming Module, Prof Andy Brass for the course work and helping us out to write codes.

### License
 - Copyright (C) 2018 University of Manchester and NHS STP 
 - Authors: Seemu Ali & Seiko Makino (github.com/seikom)