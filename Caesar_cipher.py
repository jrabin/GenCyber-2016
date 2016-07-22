# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:34:57 2016

@author: student
"""
'''
#Joelle's Encryption Code, it works well
orig_message = input("Enter your original message:")
shift = int(input("Enter your preferred shift interval:"))

def encrypt_that_thang(orig_message, shift):
    encrypted_message = ""
    for char in orig_message:
        if 65<=ord(char) and ord(char)<=90:
            newchar= ord(char)+shift
            if newchar>90:
                newchar-=26
        if 97<=ord(char) and ord(char)<=122: 
            newchar= ord(char)+shift
            if newchar>122:
                newchar-=26
        if ord(char)==32:
            newchar=32
        if ord(char)==46:
            newchar=46
        encrypted_message = encrypted_message+chr(newchar)
    return(encrypted_message)
    
print(encrypt_that_thang(orig_message, shift))

#Joelle's Decryption Code, it's messed up
encrypt_message = input("Enter the encrypted message:")

def decrypt_that_thang(encrypt_message):
    shift=1
    while shift<27:
        original_message = ""
        for char in encrypt_message:
            if 65<=ord(char) and ord(char)<=90:
                origchar=ord(char)-shift
                if origchar<65:
                    origchar+=26
                original_message+=chr(origchar)
            if 97<=ord(char) and ord(char)<=122:
                origchar=ord(char)-shift
                if origchar<97:
                    origchar+=26
                original_message+=chr(origchar)
            #if origchar<65:
                if origchar==(32-shift):
                    origchar=32
                elif origchar==(46-shift):
                    origchar=46
                else:
                    origchar+=26
            if origchar>90 and origchar<97:
                origchar+=26
            #original_message = original_message+chr(origchar)
        print(shift, original_message)
        shift+=1
decrypt_that_thang(encrypt_message)
'''
#Teacher's Code for Decryption
def decryptCC(encrypted):
    for i in range(26):
        decrypted="" #empty string for every iteration of for loop
        for char in encrypted:
            asc = ord(char)
            if asc>=65 and asc<=91:#check if upper
                asc-=i
                if asc<65:
                    asc+=26
                decrypted+=chr(asc)
            elif asc<=122 and asc>=97:#check if lower
                asc-=i
                if asc<97:
                    asc+=26
                decrypted+=chr(asc)
            else:
                decrypted+=char
        print(i, decrypted)
    return(1)
decryptCC("Zkij te yj.")
         
            



     