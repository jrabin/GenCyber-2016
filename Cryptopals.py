# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 13:04:49 2016

@author: student
"""
#Convert from hex to base 64
import base64

hex_msg="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_msg=""

decimal_char=int(hex_msg,16)
base64_msg+=chr(decimal_char)
encoded=base64.b64encode(base64_msg)
print(encoded)
    