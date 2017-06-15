#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:14:48 2017

@author: ezgi
"""

class Parent():
    print ('Parent constructor is called')
    def __init__(self,last_name,eye_color):
        self.last_name=last_name
        self.eye_color=eye_color
        
    def show_info(self):
        print("Last Name: "+ self.last_name)
        print("Eye color:"+ self.eye_color)


class Child(Parent):
    def __init__(self,last_name,eye_color,numberofToys):
        print ('Child constructor is called')
        Parent.__init__(self,last_name,eye_color) 
        self.numberofToys=numberofToys
    
    def show_info(self):
        print("Last Name: "+ self.last_name)
        print("Eye color:"+ self.eye_color)
        print("Number of Toys:"+ str(self.numberofToys))

myMom=Parent("Ozcan","brown")
myMom.show_info()

me=Child("Ozcan","brown",55)
me.show_info()