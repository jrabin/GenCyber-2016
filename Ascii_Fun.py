# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:15:15 2016

@author: student
"""

#TIME TO ASCII
#Basics
mychar=2
print(ord(mychar))

myascii = 65
print(chr(myascii))

#Ascii--> Hex
def ascii_to_hex(letter):
    '''takes a parameter a string w/ single capital
    returns a two character string with the hex rep
    of the ascii vlaue for the letter'''
    
    #constants that we will need
    ascii_val_of_A =65
    alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hex_symbols ="0123456789ABCDEF"
    
    letter_position = alphabet.find(letter)
    ascii_val_of_letter=ascii_val_of_A +letter_position
     
    left_num=ascii_val_of_letter//16
    right_num=ascii_val_of_letter%16
    
     
     
     
     
     
     
     