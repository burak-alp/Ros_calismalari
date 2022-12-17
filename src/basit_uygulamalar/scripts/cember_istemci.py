#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:48:02 2022

@author: burak
"""

import rospy
from basit_uygulamalar.srv import CemberHareket

rospy.wait_for_service("cember_servis")
try:
    yaricap=float(input("Yaricap giriniz: "))
    servis=rospy.ServiceProxy("cember_servis",CemberHareket)
    servis(yaricap)
except:
    print("Servisle alakalı sorun oluştu")