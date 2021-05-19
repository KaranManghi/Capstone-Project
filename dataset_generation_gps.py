import csv
import random

"""
1.) noise : 1-10
2.) network security : 1-10
3.) accuracy : 5-500 cm 
4.) battery consumption : 0-10
"""

with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/gps_data.csv','w',newline='') as f:
    w=csv.writer(f)

    w.writerow(['Noise','Security','Accuracy','Battery Consumption'])

    for i in range(1000):
        noise=random.randint(1,10)
        security=random.randint(1,10)
        accuracy=random.randint(5,500)
        battery=random.randint(1,10)
        

        w.writerow([noise,security,accuracy,battery])










