import csv
import random

"""
1.) object detection range : 10-150 m
2.) image sharpness : 1-10 
3.) image resolution : 200x200 - 3000x3000
4.) noise : 1-10
5.) network security : 1-10
6.) accuracy : 1-10 (based on the object detection algorithm accuracy) 
7.) battery consumption : 0-10
"""

with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/camera_data.csv','w',newline='') as f:
    w=csv.writer(f)

    w.writerow(['Detection Range','Sharpness','Image Resolution 1','Image Resolution 2','Noise','Security','Accuracy','Battery Consumption'])

    for i in range(1000):
        detection_range=random.randint(10,150)
        sharpness=random.randint(1,10)
        resolution_1=random.randint(200,3000)
        resolution_2=random.randint(200,3000)
        noise=random.randint(1,10)
        security=random.randint(1,10)
        accuracy=random.randint(1,10)
        battery=random.randint(1,10)

        w.writerow([detection_range,sharpness,resolution_1,resolution_2,noise,security,accuracy,battery])










