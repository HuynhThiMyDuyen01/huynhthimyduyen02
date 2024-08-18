# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:37:53 2024

@author: MY DUYEN
"""

GPA=float(input("nhap diem "))
if GPA<3.5:
     print("hoc luc kem ")
elif 3.5 <= GPA <5:
    print ("hoc luc yeu ")
elif 5<= GPA <7:
    print("hoc luc trung binh ")
elif 7<= GPA < 8:
    print (" hoc luc kha ")
elif 8<= GPA <9:
    print (" hoc luc gioi ")
elif 9<= GPA <=10:
    print ("hoc luc xuat sac ")
else :
    print ("khong xac dinh ")