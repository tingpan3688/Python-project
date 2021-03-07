# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:44:36 2021

@author: user
"""

user = input("帳號: ")
pw = input("密碼: ")

if (user == "Ting" and pw == "3688") or (user == "Lynn" and pw == "168"):
    print("歡迎進入系統")
    year = int( input("西元年: ") )
    
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
        print("閏年")
    else :
        print("平年")
        
else :
    print("帳號 或 密碼 錯誤")t