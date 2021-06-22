# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:23:51 2021

@author: DELL
"""

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):

    ans = 0
    for child in node.iter():
        ans += len(child.attrib)
        #print((child.attrib))
    return ans
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))