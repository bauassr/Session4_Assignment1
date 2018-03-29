# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:58:54 2018

@author: singh.shivam
"""

def words_length(words):
    s=[]
    for w in words:
        s.append(len(w))
    return s
    
Words=["Acadgild","Data","DataScience","DataMart","programming",
       "Coding","Math","Csharp","Python","R"] 
vowels = 'aeiou'
def Vowel(c):
    if c in vowels:
        return True
    else:
        return False
print(Words)    
print("length of words:-")
print(words_length(Words))

print("Enter a Character to check if it is vowel or not")

a=""
while a!="Exit":
    a=input()
    if a!="Exit":
       print(Vowel(a),":: Type Exit to terminate") 
    
print("Program terminated")
