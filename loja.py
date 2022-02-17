#!/usr/bin/python3

from mtb import MTB
from speed import Speed
from gravel import Gravel

def main():
    bike1 = MTB()
    bike2 = Speed()
    bike3 = Gravel()
    bike1.setPrice(1000)
    bike2.setPrice(2000)
    bike3.setPrice(2300)
    print ("Bicicleta 1:")
    print (bike1.getType() + " " + bike1.getDesc() + " Preço: R$" + str(bike1.getPrice()))
    print ("Bicicleta 2:")
    print (bike2.getType() + " " + bike2.getDesc() + " Preço: R$" + str(bike2.getPrice()))
    print ("Bicicleta 1:")
    print (bike3.getType() + " " + bike3.getDesc() + " Preço: R$" + str(bike3.getPrice()))
   
if __name__ == "__main__":
    main()
