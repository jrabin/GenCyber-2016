# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:51:11 2016

@author: student
"""
'''
for i in range (1,11): #using function range (1st parameter is start, 2nd parameter is end, 3rd parameter is interval)
    print(i)
    
for i in range(1, 11, -1): #negative number should make it print backwards
    print(i)
    
string = "Do you wanna be my lover?"

for char in string: #goes through each character in the string
    print (char)

def ascii_to_eight_bit(letter):
    num = ord(letter)
    bitstring=""
    for i in range (8):
        print(num)
        if num%2==0:
            bitstring = '0'+bitstring
            print('0')
        else:
            bistring='1'+bitstring
            print('1')
        num=num//2
    return bistring
print(ascii_to_eight_bit('S'))
'''
#Write a function to check whether a password follows these rules:
#@ least 6 characters long, @ least 1 capital letter, @ least 1 lowercase letter
#return true if password works


def password_requirements(password):
    password=input("Set your password:")

    length=False
    capital=False
    lowercase=False

    if len(password)>=6:
        length=True
    
    for char in password:
        if 65 <= ord(char) and ord(char) <= 90:
            capital=True
        elif 97<= ord(char) and ord(char) <=122:
            lowercase=True
    if length==True and capital==True and lowercase==True:
        return True
        print("Your password is good")
    else:
        print("Your password must be @ least 6 characters long, have @ least 1 capital letter, and have @ least 1 lowercase letter")
        return False

print(password_requirements(password))

'''
#Correct Version of Password Check Function
def check_password(password):
    hasUpper=False
    hasLower=False
    if len(password)>=6:
        for char in password:
            if ord(char)>=65 and ord(char)<=90:
                hasUpper=True
            elif ord(char)>= 97 and ord(char)<=122:
                hasLower=True
        if hasUpper==True and hasLower==True:
            return True
        else:
            return False
    else:
        return False
print(check_password("Paramore"))
print(check_password("sdfsdgdfs"))
'''        



