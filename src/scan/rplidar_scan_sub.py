#!/usr/bin/env python  
""" 

- Version 1.0 2015/3/11

this code subscribe to rplidar_scan_pub
    

Copyright (c) 2015 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify it

This programm is tested on kuboki base turtlebot. 

"""

import rospy 
from sensor_msgs.msg import LaserScan

def callback(data):
 
 print data
 print 'data lenth:',len(data.ranges),'\n'
 a=[]
 if data.intensities:
  for i in range(len(data.ranges)):
   a.append([data.ranges[i],data.intensities[i]])
  print a

def listener():
 print "start listening to rplidar"
 rospy.init_node('rplidar_wrapper', anonymous=False)
 rospy.Subscriber("/scan", LaserScan, callback)
 rospy.spin()

if __name__ == '__main__':
 listener()

 
