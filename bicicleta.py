#!/usr/bin/python3

class Bycicle:

    def __init__(self,bikeType):
        self.m_type = bikeType
        self.m_price = 0
        self.m_description = ""

    def getType(self):
        return self.m_type

    def getPrice(self):
        return self.m_price

    def setPrice(self, price=0):
        self.m_price = price

    def setDesc(self,desc):
        self.m_description = desc

    def getDesc(self):
        return self.m_description

