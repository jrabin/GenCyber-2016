# -*- coding: utf-8 -*-
"""
Joelle Rabin- Court
GenCyber 2016
Created on Fri Jul  8 13:14:36 2016
Intro to Hash
"""
#Adding the hash library
import hashlib

#Begin defining your md5 hash
def md5(fname):
    #Prepare to hash
    hash_md5 = hashlib.md5()
    #Open a file
    with open(fname, "rb") as f:
        #For each 4096 byte chunk of the file
        for chunk in iter(lambda: f.read(4096), b""):
            #HASH IT UP IN HERE!
            hash_md5.update(chunk)
    #Give me the hash back pls, return it
    return hash_md5.hexdigest()
#Objective find two files that look the same but have diff hashes
print(md5("/home/student/Desktop/facebook_is_lame.jpg"))
print(md5("/home/student/Desktop/wishing_to_shave.jpg"))
#^^^Look almost the same, but have diff hashes, revealed secret message "Hi"

print(md5("/home/student/Desktop/looking_fresh.jpg"))
print(md5("/home/student/Desktop/my_speech.jpg"))
print(md5("/home/student/Desktop/ocean_breeze.jpg"))
print(md5("/home/student/Desktop/whitest_shirt_ever.jpg"))
print(md5("/home/student/Desktop/myspace_profile_pic.jpg"))
print(md5("/home/student/Desktop/throwback.jpg"))

#in lenox there is a command that does this called md5sum bork.jpg