# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:14:27 2024

@author: MY DUYEN
"""

distance=float(input("nhap do dai doan duong (m):"))
if distance < 300:
    print("duong den truong qua gan. Thoi! Di bo")
elif distance > 1200:
    print("duong den truong qua xa.Thoi! Di xe may ")
elif distance >=300 and distance <=700:
        print("duong den truong khong xa.Thoi! Di xe dap ") 
else:
    print("khong xac dinh")