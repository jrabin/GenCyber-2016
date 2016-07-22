# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:11:54 2016

@author: student
"""
#A more in-depth look at string indexing
#Remeber: all white spaces are also counted as characters

strng= "Pokemon GO is addicting"
print(strng[8])

#print(strng[8:13])
#the colon : indicates range, from 8th character to 13th character

seg = strng[8:13]
print(seg)

#prints from placement 8 to the end
print(strng[8:]) 

 #prints from beginning to placement 13
print(strng[:13])

print(strng[-1:])
print(strng[-1]) #with negative numbers, starts from -1 at the right
print(len(strng))

