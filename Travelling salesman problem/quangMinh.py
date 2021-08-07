# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:05:43 2021

@author: dinhm
"""


import TSP
import time

file = input('Enter filename: ')
startCity = int(input('Enter start city (0 to 9): '))
print('')

myTsp = TSP.tsp(file)
myTsp.computeDistances()
myTsp.computeGreedyTour(startCity)
myTsp.printCityInformation()
myTsp.printDistances()
myTsp.printTour()
myTsp.plot()

print ("\nProgrammed by Dinh Quang Minh")
print ("Date: " + time.ctime())
print ("End of processing")