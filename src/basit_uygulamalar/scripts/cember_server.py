#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:21:51 2022

@author: burak
"""

import rospy
from basit_uygulamalar.srv import CemberHareket
from geometry_msgs.msg import Twist

def cemberFonksiyonu(istek):
    hiz_mesaji=Twist()
    lineer_hiz=1.0
    hiz_mesaji.linear.x=lineer_hiz
    yaricap=istek.yaricap
    hiz_mesaji.angular.z=lineer_hiz/yaricap
    
    while not rospy.is_shutdown():
        pub.publish(hiz_mesaji)
rospy.init_node("cember_hareket")
pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
rospy.Service("cember_servis",CemberHareket,cemberFonksiyonu)
rospy.spin()
