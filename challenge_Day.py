# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 10:15:35 2016

@author: student
"""

msg="hi"
bin_msg=""
for char in msg:
    asc_val=int(ord(char))
    bin_msg+=bin(asc_val)
print(bin_msg)
    