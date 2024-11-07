# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:54:25 2024

@author: Huỳnh Như Ngọc
"""
#Viết lệnh kiểm tra giá trị nhập vào từ bàn phím thỏa điều kiện thuộc
#[-99; 99]. Nếu không khỏa bắt người dùng nhập lại đến khi nào
#khỏa điều kiện

def gia_tri():
    while True:
    
            num=int(input("nhap mot so trong khoan [-99,99]:"))
            if -99<=num<=99:
                
                print("gia tri ban nhap hop le!")
                break
            else:
                print("do khong phai la so hop le. vui long nhap lai")
                
if __name__=="__main__":
 gia_tri()                
            