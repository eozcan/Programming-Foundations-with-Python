#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:19:43 2017

@author: ezgi
"""
import urllib

def read_text():
    quotes=open("/Users/ezgi/Desktop/python/movie_quotes.txt")
    contents_of_file=quotes.read()
    quotes.close()
    check_profanity(contents_of_file)
    
    

def check_profanity(contents):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + urllib.parse.urlencode([('q', contents)]))
    output=connection.read()
    if b"true" in output:
        print ('Profanity Alert!')
    elif b"false" in output:
        print ('No curse words!')
    else:
        print ('Could not scan properly')
    connection.close()
    
read_text()


##URLs cannot have many special characters in them (like spaces), and those need to be encoded to be a valid url (like replaceing space with +).

##So basically, the content you read from the file is not encoded to be a proper http url. That is done by urllib.parse.urlencode.

