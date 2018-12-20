
"""
test_LRGParser.py 

Authors: Seemu Ali, Seiko Makino 
Date: 20th  Dec 2018

Purpose: to test LRGparser script on LRG1 and LRG2 xml file 

test run on python version 3.7.0
"""


import pytest

from LRGParser import geneinfo, exoninfo
import xml.etree.ElementTree as ET
import sys 


# test if geneinfo function returns correct gene information for both LRG_1 and LRG_2 file (e.g chromosome number, start pos, end pos, reverse (-1) or forward (1) strand)
def test_geneinfo():
    tree=ET.parse('LRG_1.xml')
    root = tree.getroot()
    assert geneinfo(root) == (17, 48259457, 48284000, "-1")
    tree=ET.parse('LRG_2.xml')
    root = tree.getroot()
    assert geneinfo(root) == (7, 94018873, 94062544, "1")

# to ensure raise function in else command within exoninfo function is working 
#to assert that label, start and end positions are correctly appended into empty list 
def test_exoninfo():
    with pytest.raises(ValueError):
    	tree=ET.parse('LRG_1.xml')
    	root = tree.getroot()
    	exoninfo (root,[],[],[], '2', 48259457, 48284000)
    assert exoninfo(root,[],[],[], '-1', 48259457, 48284000) == (['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51'], [48279000, 48277308, 48276951, 48276814, 48276688, 48275865, 48275566, 48275363, 48275146, 48274594, 48274424, 48274031, 48273889, 48273728, 48273560, 48273337, 48273026, 48272839, 48272691, 48272461, 48272189, 48271987, 48271808, 48271544, 48271402, 48270408, 48270211, 48270054, 48269889, 48269385, 48269247, 48268851, 48268285, 48267957, 48267741, 48267469, 48267273, 48267093, 48266899, 48266636, 48266371, 48266156, 48265998, 48265510, 48265344, 48264898, 48264483, 48264283, 48263868, 48263381, 48263009], [48278772, 48277114, 48276917, 48276779, 48276587, 48275794, 48275522, 48275310, 48275093, 48274541, 48274371, 48273978, 48273845, 48273675, 48273516, 48273284, 48272928, 48272795, 48272593, 48272408, 48272082, 48271934, 48271710, 48271491, 48271304, 48270355, 48270158, 48270001, 48269836, 48269341, 48269149, 48268744, 48268178, 48267904, 48267688, 48267362, 48267220, 48267040, 48266738, 48266529, 48266264, 48266103, 48265891, 48265457, 48265237, 48264845, 48264376, 48264001, 48263678, 48263139, 48261457])


