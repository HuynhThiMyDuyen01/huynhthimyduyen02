# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:25:27 2024

@author: MY DUYEN
"""


import random
chon=["keo", "bua ", "bao"]
you=input("nhap lua chon cua ban (keo,bua,bao)")
computer=random.choice(chon)
print("May : ",computer)
if you not in chon:
    print("lua chon cua ban khong hop le .") 
else:
    if you==computer:
        print("hoa ")
    elif (you == "keo " and computer == "bao") or \
         (you == "bua " and computer == "keo") or \
         (you == "bao " and computer == "bua"):
        print("You win")
    else:
        print("Computer win")