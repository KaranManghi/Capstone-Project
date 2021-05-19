import csv
import random

"""
1.) object detection range : 10-600 m
2.) noise : 1-10
3.) network security : 1-10
4.) accuracy : 1-10 (based on the object detection algorithm accuracy) 
5.) battery consumption : 1-10
6.) radarsExist : True or False
"""

with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/radar_data.csv','w',newline='') as f:
    w=csv.writer(f)

    w.writerow(['Detection Range','Noise','Security','Accuracy','Battery Consumption','OtherRadarsPresent'])

    for i in range(1000):
        detection_range=random.randint(10,600)
        noise=random.randint(1,10)
        security=random.randint(1,10)
        accuracy=random.randint(1,10)
        battery=random.randint(1,10)
        radarsExist=random.randint(0,1)

        w.writerow([detection_range,noise,security,accuracy,battery,radarsExist])










