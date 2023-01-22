# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 19:51:01 2022

@author: Dell
"""

import math
from datetime import datetime
name=input("enter your name:")
def bill():
    a=True
    total_price=0
    list_item_price=[]
    while a:
        print('''
              1.list of items
              2.choose item
              3.exit
              ''')
        choice=int(input("enter your choice:"))  
        choices=[1,2,3]
        if choice in choices:
            d={'Tamarind':70,'oil':120,'mirchi':130,'rice':40,'shampoo':20,
               'soap':30}
            if choice==1:
                c=1
                for i,j in d.items():
                    print("\t",c,'.',i,'$',j)
                    c+=1
            if choice==2:
                q=True
                while q:
                    print("press q to see main menu")
                    item=input("enter item")
                    if item in d.keys():
                        quantity=input('enter quantity')
                        if quantity.isdigit():
                            print(d[item])
                            price=int(d[item]*int(quantity))
                            list_item_price.append((item,quantity,price))
                            total_price+=price
                        else:
                            print("Invalid input quantity")
                    elif item=='q':
                       q=False
                    else:
                       print("Item is not present.")
        if choice==3:
            a=False
    else: 
        print("Invalid input..please enter a valid input")
    return total_price,"Thank you,please visit again.",list_item_price  
total,msg,item_price=bill()  
if total!=0:
    print("\n")
    print('''
                   RAGHU Stores
                 Hyderabad,50010
          ''')
    print('customer Name:',name,'\t','Date:',datetime.now())    
    print(20*"==")
    for j in item_price:
        print('Item:',j[0],'\tquantity:',j[1],'Price:',j[2])
    gst=total*0.1
    gst=math.ceil(gst)
    print(18*"==")
    print("GST: RS",float(gst))
    print('Total payable amount: RS',float(gst+total))  
    print(18*"==")
    print('=====',msg,"======")
else:
    print("Hey, You weren't Bought anything...Please Buy something you want.")
    bill(11)
    
                        
                       
                        
