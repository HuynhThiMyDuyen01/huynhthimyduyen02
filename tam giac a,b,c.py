# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:42:50 2024

@author: MY DUYEN
"""

a=float(input("nhap a :"))
b=float(input("nhap b :"))
c=float(input("nhap c :"))
if a+b>c and a+c>b and b+c>a:
    print(" a,b,c là 3 canh cua tam giac ")
    if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
        print("tam giac vuong ")
    elif a==b==c:
        print("tam giac deu  ")
    elif a==b or b==c or c==a:
        print ("tam giac can ")
    else:
        print ("tam giac thuong  ")
else:
    print("a,b,c không phải là 3 canh cua tam giac ")