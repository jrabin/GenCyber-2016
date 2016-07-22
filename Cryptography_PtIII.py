# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:12:21 2016

@author: student
"""
'''
#To encode qrcode:
import qrcode
img = qrcode.make("Potatoes can sing quite well.")
img.show()
img.save('potatoes.png')

#To decode qrcode:

import qrtools
qr = qrtools.QR()
wr.decode("IMGNAME.PNG")
print(qr.data)
'''

#To encode base 64:
import base64
encoded=base64.b64encode(b'Potatoes can sing quite well.')
print(encoded)
