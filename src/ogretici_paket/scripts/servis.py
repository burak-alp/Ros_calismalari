#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:32:23 2022

@author: burak
"""
import rospy
from ogretici_paket.srv import GecenZaman

def gecenZamanFonksiyonu(istek):
    robot_hiz=0.5
    sure=istek.hedef_konum/robot_hiz
    return sure



def cevapGonder():
    rospy.init_node("server_dugum")
    rospy.Service("zaman",GecenZaman,gecenZamanFonksiyonu)
    rospy.spin()
cevapGonder()
