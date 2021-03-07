# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:08:07 2021

@author: user
"""

score = int( input("請輸入成績: ") )

if score >= 60 :
    print("及格")
else :
    print("不及格")
    
if score >= 90 :
    print("優")

if score >= 80 and score <= 89 :
    print("甲")
    
if score >= 70 and score <= 79 :
    print("乙")
    
if score >= 60 and score <= 69 :
    print("丙")
    
if score < 60 :
    print("丁")
