# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:39:14 2021

@author: DELL
"""
import re
def fun(s):
    # return True if s is a valid email, else return False
    pattern = r'[a-zA-Z][\w\_\-]*[@][a-zA-Z0-9]+[\.][a-zA-Z]{1,3}$'
    return re.match(pattern,s)
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)