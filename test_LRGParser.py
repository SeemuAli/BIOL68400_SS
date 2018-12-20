
import pytest

from lrg2bed_test3 import geneinfo, exoninfo
import xml.etree.ElementTree as ET
import sys 



def test_geneinfo():
    tree=ET.parse('LRG_1.xml')
    root = tree.getroot()
    assert geneinfo(root) == (17, 48259457, 48284000, "-1")
    tree=ET.parse('LRG_2.xml')
    root = tree.getroot()
    assert geneinfo(root) == (7, 94018873, 94062544, "1")

def test_exoninfo():
    with pytest.raises(ValueError):
    	tree=ET.parse('LRG_1.xml')
    	root = tree.getroot()
    	exoninfo (root,[],[],[], '2', 48259457, 48284000)


