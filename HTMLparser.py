# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:49:33 2021

@author: DELL
"""
import sys
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):  
    def __init__(self):
    #Since Python 3, we need to call the __init__() function of the parent class
        super().__init__()
        self.reset()
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        #Checking for attributes
        for att in attrs:
            print("-->",att[0],'>',att[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        #Checking for attributes
        for att in attrs:
            print("->",att[0],'>',att[1])
    def handle_comment(self, data):
        pass

# instantiate the parser and fed it some HTML

#line = ''.join(input() for _ in range(int(input())))
line = sys.stdin.read()
#print(line)
parser = MyHTMLParser()
parser.feed(line)