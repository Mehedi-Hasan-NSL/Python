# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:29:27 2021

@author: DELL
"""
import re
import email.utils
#print (email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
#print (email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))

#reex pattern for email 
pattern = r'^[a-zA-Z][\w\-.\.\-]*[@][a-zA-Z]+[\.][a-zA-Z]{1,3}$'
for _ in range(int(input())):
  #parsing name email from input
  uname, uemail = email.utils.parseaddr(input())
  
  #checking for a valid email
  if re.match(r'^[a-zA-Z][\w\-.\.\-]*[@][a-zA-Z]+[\.][a-zA-Z]{1,3}$',email):
     print(email.utils.formataddr((uname, uemail)))

