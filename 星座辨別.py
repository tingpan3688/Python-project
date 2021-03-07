# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:21:51 2021

@author: user
"""

month = int( input("請輸入生日月分: ") )
day = int( input("請輸入生日日期: ") )
sex = input ("請輸入性別 (F=女性 M=男性): ")

if sex == "M" :
    gender = "男"
else:
    gender = "女"
    
if month == 1 :
    if day >= 21 :
        print("水瓶" + gender)
    else:
        print("魔羯" + gender)
        
if month == 2 :
    if day >= 20 :
        print("雙魚" + gender)
    else:
        print("水瓶" + gender)
        
if month == 3 :
    if day >= 21 :
        print("牡羊" + gender)
    else:
        print("雙魚" + gender)

if month == 4 :
    if day >= 20 :
        print("金牛" + gender)
    else:
        print("牡羊" + gender)

if month == 5 :
    if day >= 21 :
        print("雙子" + gender)
    else:
        print("金牛" + gender) 
        
if month == 6 :
    if day >= 22 :
        print("巨蟹" + gender)
    else:
        print("雙子" + gender)
        
if month == 7 :
    if day >= 23 :
        print("獅子" + gender)
    else:
        print("巨蟹" + gender)
        
if month == 8 :
    if day >= 23 :
        print("處女" + gender)
    else:
        print("獅子" + gender)
        
if month == 9 :
    if day >= 23 :
        print("天秤" + gender)
    else:
        print("處女" + gender)
        
if month == 10 :
    if day >= 24 :
        print("天蠍" + gender)
    else:
        print("天秤" + gender)
        
if month == 11 :
    if day >= 22 :
        print("射手" + gender)
    else:
        print("天蠍" + gender)
        
if month == 12 :
    if day >= 21 :
        print("魔羯" + gender)
    else:
        print("射手" + gender)
        
