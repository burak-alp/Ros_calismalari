#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 03:44:41 2022

@author: burak
"""
import rospy
from ogretici_paket.msg import Batarya_Durum

def bataryaFonksiyon(mesaj):
    rospy.loginfo("Robot şarjı: %s"%mesaj.batarya)

def mesajDinle():
    rospy.init_node("abone_dugum")
    rospy.Subscriber("batarya_konusu",Batarya_Durum,bataryaFonksiyon)
    rospy.spin()
mesajDinle()