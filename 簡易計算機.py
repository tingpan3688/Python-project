# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

pw = input("請輸入密碼")

if pw != "ABC123" :
    print("密碼錯誤，程式結束")    

    
if pw == "ABC123" :
    print("歡迎進入系統!")

    num1 = int( input("請輸入數字1: "))
    num2 = int( input("請輸入數字2: "))
    func = input("請輸入要執行的運算(+-*/): ")

    if func == "+" :
        print(num1 + num2)
    
    if func == "-" :
        print(num1 - num2)
    
    if func == "*" :
        print(num1 * num2)
    
    if func == "/" :
        print(num1 / num2)
