#!/usr/bin/python
# coding: utf-8

# VL53L0X -ToF sensor
from sensor import sensor

class ToF(sensor):
    def __init__(self):
        self.ToF = sensor()
    def ReadDistance(self):
        LOOP = 5
        tmp = 0.0
        for i in xrange(LOOP):
            data = self.ToF.ReadDistance()
            if data!=None:
                tmp += data
        Distance =  float(tmp) / float(LOOP)
        print Distance
if __name__ == '__main__':
    TOF = ToF()
    while True:
        TOF.ReadDistance()
