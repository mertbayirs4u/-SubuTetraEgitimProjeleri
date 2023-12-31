#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class carpmadanDur:
    def __init__(self):
        rospy.init_node('carpmadan_dur')
        self.laser_scan = LaserScan()
        self.hiz = Twist()
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.lazerCallback)
        rospy.spin()
    
    
    def lazerCallback(self, scan):
        sol_on = list(scan.ranges[0:9])
        sag_on = list(scan.ranges[350:359])
        on = sol_on + sag_on
        sol = list(scan.ranges[80:100])
        sag = list(scan.ranges[260:280])
        min_on = min(on)
        min_sol = min(sol)
        min_sag = min(sag)
    
        if min_on > 1.0: 
                self.hiz.linear.x = 0.3
                self.hiz.angular.z = 0.0
                self.pub.publish(self.hiz)
                rospy.loginfo('Hareket Ediliyor...')

        else:
                self.hiz.linear.x = 0.0
                self.hiz.angular.z = 0.0
                self.pub.publish(self.hiz)
                rospy.loginfo('Cisim Var, Devam Edilemiyor..!')
            
               
carpmadanDur()

        
         
        
        
        
        
        
        
        
