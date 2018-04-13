#!/usr/bin/python
# coding: utf-8

# VL53L0X -ToF sensor
from sensor import sensor
import time

class ToF(sensor):
    def __init__(self):
        self.ToF = sensor()
    def ReadDistance(self):
        start = time.time()
        #calib_x = [-18, -18, -19, -20, -33, -41, -29, -29, -28, -28]
        LOOP = 4
        tmp = 0.0
        for i in xrange(LOOP):
            tmp += float(self.ToF.ReadDistance())
        Distance =  tmp / float(LOOP)
        print Distance
if __name__ == '__main__':
    TOF = ToF()
    TOF.ReadDistance()
