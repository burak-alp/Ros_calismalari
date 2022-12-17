#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:30:13 2022

@author: burak
"""
import rospy
from geometry_msgs.msg import Twist

def Volta():
    rospy.init_node("volta_at")
    pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
    hiz_mesaji=Twist()
    robot_hizi=0.25
    volta_uzunluk=rospy.get_param("/VoltaUzunluk")
    volta_sayisi=rospy.get_param("/VoltaSayisi")
    sayici=0
    rospy.loginfo("devriye gezmeye başlandı")
    
    while sayici<volta_sayisi:
        t0=rospy.Time.now().to_sec()
        yer_degistirme=0
        if sayici %2==0:
            hiz_mesaji.linear.x=robot_hizi
        else:
            hiz_mesaji.linear.x=-robot_hizi
        while yer_degistirme < volta_uzunluk:
            pub.publish(hiz_mesaji)
            t1=rospy.Time.now().to_sec()
            yer_degistirme=robot_hizi*(t1-t0)
        hiz_mesaji.linear.x=0
        pub.publish(hiz_mesaji)
        sayici=sayici+1
    rospy.loginfo("devriye tamamlandı")
    rospy.is_shutdown()

Volta()
## paramlar terminalden yüklenecek
