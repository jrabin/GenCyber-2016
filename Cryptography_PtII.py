# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:55:57 2016

@author: student
"""

p=37
q=41
n=1517
t=1440
e=1019
d=1139


p=int(input("Give me a prime number:"))
q=int(input("Give me another prime number:"))
n=p*q
print("n=",n)
t=(p-1)(q-1)
print("t=",t)



'''for e in range(n):
    e+=1
    if t%e!=0:
        print(e)'''

'''for d in range(2000):
    if (e*d)% t == 1:
        print(d)'''

m="My tummy hurts."
c=""
for letter in m:
    ascii_letter=int(ord(letter))
    encryp_let = (ascii_letter**e)%n
    c= c+ " "+str(encryp_let)
print(c)
    
    
    
    
