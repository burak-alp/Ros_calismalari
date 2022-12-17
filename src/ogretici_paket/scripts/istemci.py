#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:40:10 2022

@author: burak
"""
import rospy
from ogretici_paket.srv import GecenZaman

def istekteBulun(x):
    rospy.wait_for_service("zaman")
    try:
        servis=rospy.ServiceProxy("zaman",GecenZaman)
        cevap=servis(x)
        return cevap.gecen_sure
    except rospy.ServiceException:
        print("servisle alakalı sorun oluştu")
        
hedef=float(input("hedef konumunu giriniz:"))
t=istekteBulun(hedef)
print("hedefe varana kadar gecen süre:",t)
        
