import csv
import random

"""
1.) object detection range : 10-570 m
2.) channels : 1,16,32,64 
3.) dust resistance : 1-10
4.) noise : 1-10
5.) network security : 1-10
6.) accuracy : 1-10 
7.) battery consumption : 1-10
8.) isSunBright : True or False
"""

with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/lidar_data.csv','w',newline='') as f:
    w=csv.writer(f)

    w.writerow(['Detection Range','Channels','Dust Resistance','Noise','Security','Accuracy','Battery Consumption','IsSunBright'])

    for i in range(1000):
        detection_range=random.randint(10,570)
        channels=random.choice([1,16,32,64])
        dust_resistance=random.randint(1,10)
        noise=random.randint(1,10)
        security=random.randint(1,10)
        accuracy=random.randint(1,10)
        battery=random.randint(1,10)
        isSun=random.randint(0,1)

        w.writerow([detection_range,channels,dust_resistance,noise,security,accuracy,battery,isSun])










