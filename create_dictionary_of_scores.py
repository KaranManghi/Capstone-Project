from collections import defaultdict
import csv
import time
import pickle
"""
Key factors : 
1.) Range
2.) Noise
3.) Battery Consumption
4.) Accuracy

Deciding factor:
1.)Final Score

Each sensor also has some other factors in addition to the key factors which will decide the final score
"""

class lidar:
    def __init__(self,detection_range,channels,dust_resistance,noise,security,accuracy,battery_consumption,isSun):
        self.type="lidar"
        self.detection_range=detection_range
        self.channels=channels
        self.dust_resistance=dust_resistance
        self.noise=noise
        self.security=security
        self.accuracy=accuracy
        self.battery_consumption=battery_consumption
        self.isSun=isSun
        self.score=None

        self.default_detection_range_weightage=0.2
        self.default_channels_weightage=0.1
        self.default_dust_resistance_weightage=0.05
        self.default_noise_weightage=0.05
        self.default_security_weightage=0.2
        self.default_accuracy_weightage=0.3
        self.default_battery_consumption_weightage=0.1

class camera:
    def __init__(self,detection_range,sharpness,resolution1,resolution2,noise,security,accuracy,battery_consumption):
        self.type="camera"
        self.detection_range=detection_range
        self.sharpness=sharpness
        self.resolution1=resolution1
        self.resolution2=resolution2
        self.noise=noise
        self.security=security
        self.accuracy=accuracy
        self.battery_consumption=battery_consumption
        self.score=None

        self.default_detection_range_weightage=0.05
        self.default_sharpness_weightage=0.025
        self.default_resolution_weightage=0.025
        self.default_noise_weightage=0.1
        self.default_security_weightage=0.2
        self.default_accuracy_weightage=0.5
        self.default_battery_consumption_weightage=0.1

class radar:
    def __init__(self,detection_range,noise,security,accuracy,battery_consumption,radarsExist):
        self.type="radar"
        self.detection_range=detection_range
        self.noise=noise
        self.security=security
        self.accuracy=accuracy
        self.battery_consumption=battery_consumption
        self.radarsExist=radarsExist
        self.score=None

        self.default_detection_range_weightage=0.2
        self.default_noise_weightage=0.2
        self.default_security_weightage=0.2
        self.default_accuracy_weightage=0.3
        self.default_battery_consumption_weightage=0.1

class gps:
    def __init__(self,noise,security,accuracy,battery_consumption):
        self.type="gps"
        self.noise=noise
        self.security=security
        self.accuracy=accuracy
        self.battery_consumption=battery_consumption
        self.score=None

        self.default_noise_weightage=0.2
        self.default_security_weightage=0.2
        self.default_accuracy_weightage=0.5
        self.default_battery_consumption_weightage=0.1

start_time=time.clock()
sensor_dictionary=defaultdict()

"""initializing the dictionary of sensors with empty lists which will be filles with respective sensor objects upon reading the csv files
""" 
sensor_dictionary['camera']=[]
sensor_dictionary['lidar']=[]
sensor_dictionary['radar']=[]
sensor_dictionary['gps']=[]

# the available modes:
modes=['high security','high accuracy','low battery consumption']

# the max weight which can be assigned to the high priority category. If multiple categories, this weight will be divided equally amonng them
max_weight=0.9

#supplied by the user defining which particular feature should be kept in mind while selecting sensors
modes_to_apply=["high security"]

modes_to_apply_set=set([])

for i in range(len(modes_to_apply)):
    if modes_to_apply[i] == "high security":
        modes_to_apply_set.add("security")
    elif modes_to_apply[i] == "high accuracy":
        modes_to_apply_set.add("accuracy")
    elif modes_to_apply[i] == "low battery consumption":
        modes_to_apply_set.add("battery_consumption")

#add camera csv data to the dictionary 
with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/camera_data.csv','r') as f:
    w=csv.reader(f,delimiter=',')
    next(w)

    for r in w:
        # print(r)
        camera_sensor=camera(int(r[0]),int(r[1]),int(r[2]),int(r[3]),int(r[4]),int(r[5]),int(r[6]),int(r[7]))
        if len(modes_to_apply_set)!=0:
            weight_for_each=max_weight/len(modes_to_apply)

            temp_set_all=set(["detection_range","sharpness","resolution","noise","security","accuracy","battery_consumption"])

            remaining_set = temp_set_all-modes_to_apply_set

            other_weights=0.1/len(remaining_set)

            for n in modes_to_apply_set:
                if n=="security":
                    camera_sensor.default_security_weightage=weight_for_each
                    # print("camera_sensor.default_security_weightage is ",camera_sensor.default_security_weightage)
                elif n=="accuracy":
                    camera_sensor.default_accuracy_weightage=weight_for_each
                elif n=="battery_consumption":
                    camera_sensor.default_battery_consumption_weightage=weight_for_each
            
            for n in remaining_set:
                if n=="security":
                    camera_sensor.default_security_weightage=other_weights
                elif n=="accuracy":
                    camera_sensor.default_accuracy_weightage=other_weights
                    # print("camera_sensor.default_accuracy_weightage is ",camera_sensor.default_accuracy_weightage)
                elif n=="battery_consumption":
                    camera_sensor.default_battery_consumption_weightage=other_weights
                    # print("camera_sensor.default_battery_consumption_weightage is ",camera_sensor.default_battery_consumption_weightage)
                elif n=="detection_range":
                    camera_sensor.default_detection_range_weightage=other_weights
                    # print("camera_sensor.default_detection_range_weightage is ",camera_sensor.default_detection_range_weightage)
                elif n=="sharpness":
                    camera_sensor.default_sharpness_weightage=other_weights
                    # print("camera_sensor.default_sharpness_weightage is ",camera_sensor.default_sharpness_weightage)
                elif n=="resolution":
                    camera_sensor.default_resolution_weightage=other_weights
                    # print("camera_sensor.default_resolution_weightage is ",camera_sensor.default_resolution_weightage)
                elif n=="noise":
                    camera_sensor.default_noise_weightage=other_weights
                    # print("camera_sensor.default_noise_weightage is ",camera_sensor.default_noise_weightage)

        max_res=3000*3000
        min_res=200*200
        scale_min=1
        scale_max=10

        # print(camera_sensor.resolution[1])
        curr_res=int(camera_sensor.resolution1) * int(camera_sensor.resolution2)
        res_score= ((((scale_max-scale_min) * (curr_res-min_res))/(max_res-min_res)) + scale_min)*camera_sensor.default_resolution_weightage

        maximum_detection_range=150
        minimum_detection_range=10

        curr_detection_range=camera_sensor.detection_range
        detect_range_score=((((scale_max-scale_min) * (curr_detection_range-minimum_detection_range))/(maximum_detection_range-minimum_detection_range)) + scale_min)*camera_sensor.default_detection_range_weightage

        # print("camera_sensor.security is ",camera_sensor.security*camera_sensor.default_security_weightage)
        # print("camera_sensor.accuracy is ",camera_sensor.accuracy*camera_sensor.default_accuracy_weightage)
        # print("camera_sensor.battery_consumption is ",camera_sensor.battery_consumption*camera_sensor.default_battery_consumption_weightage)
        # print("camera_sensor.detection_range is ",detect_range_score)
        # print("camera_sensor.sharpness is ",camera_sensor.sharpness * camera_sensor.default_sharpness_weightage)
        # print("camera_sensor.noise is ",camera_sensor.noise*camera_sensor.default_noise_weightage)
        # print("res is ",res_score)


        camera_sensor.score=(camera_sensor.security*camera_sensor.default_security_weightage) + (camera_sensor.accuracy*camera_sensor.default_accuracy_weightage) + (camera_sensor.battery_consumption*camera_sensor.default_battery_consumption_weightage) + detect_range_score + (camera_sensor.sharpness * camera_sensor.default_sharpness_weightage) + res_score + (camera_sensor.noise*camera_sensor.default_noise_weightage)
        
        # print(camera_sensor.score)

        sensor_dictionary['camera'].append(camera_sensor)



# print(sensor_dictionary['camera'][0].detection_range)


#add lidar csv data to the dictionary 
with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/lidar_data.csv','r') as f:
    w=csv.reader(f,delimiter=',')
    next(w)

    for r in w:
        lidar_sensor=lidar(int(r[0]),int(r[1]),int(r[2]),int(r[3]),int(r[4]),int(r[5]),int(r[6]),bool(r[7]))
        # noise_flag=False
        # if lidar_sensor.isSun==1:
        #     noise_flag=True
        #     lidar_sensor.noise=2
        #     modes_to_apply_set.add("noise")
        
        if len(modes_to_apply_set)!=0:
            
            weight_for_each=max_weight/len(modes_to_apply)

            temp_set_all=set(["detection_range","channels","dust_resistance","noise","security","accuracy","battery_consumption"])

            remaining_set = temp_set_all-modes_to_apply_set

            other_weights=0.1/len(remaining_set)

            for n in modes_to_apply_set:
                if n=="security":
                    lidar_sensor.default_security_weightage=weight_for_each
                    # print("camera_sensor.default_security_weightage is ",camera_sensor.default_security_weightage)
                elif n=="accuracy":
                    lidar_sensor.default_accuracy_weightage=weight_for_each
                elif n=="battery_consumption":
                    lidar_sensor.default_battery_consumption_weightage=weight_for_each
            
            for n in remaining_set:
                if n=="security":
                    lidar_sensor.default_security_weightage=other_weights
                elif n=="accuracy":
                    lidar_sensor.default_accuracy_weightage=other_weights
                    # print("camera_sensor.default_accuracy_weightage is ",camera_sensor.default_accuracy_weightage)
                elif n=="battery_consumption":
                    lidar_sensor.default_battery_consumption_weightage=other_weights
                    # print("camera_sensor.default_battery_consumption_weightage is ",camera_sensor.default_battery_consumption_weightage)
                elif n=="detection_range":
                    lidar_sensor.default_detection_range_weightage=other_weights
                    # print("camera_sensor.default_detection_range_weightage is ",camera_sensor.default_detection_range_weightage)
                elif n=="channels":
                    lidar_sensor.default_channels_weightage=other_weights
                    # print("camera_sensor.default_sharpness_weightage is ",camera_sensor.default_sharpness_weightage)
                elif n=="dust_resistance":
                    lidar_sensor.default_dust_resistance_weightage=other_weights
                    # print("camera_sensor.default_resolution_weightage is ",camera_sensor.default_resolution_weightage)
                elif n=="noise":
                    lidar_sensor.default_noise_weightage=other_weights
                    # print("camera_sensor.default_noise_weightage is ",camera_sensor.default_noise_weightage)

        if lidar_sensor.isSun==1:
            lidar_sensor.noise=2

        scale_min=1
        scale_max=10

        minimum_channels=1
        maximum_channels=64

        maximum_detection_range=570
        minimum_detection_range=10

        curr_detection_range=lidar_sensor.detection_range
        detect_range_score=((((scale_max-scale_min) * (curr_detection_range-minimum_detection_range))/(maximum_detection_range-minimum_detection_range)) + scale_min)*lidar_sensor.default_detection_range_weightage

        curr_channels=lidar_sensor.channels
        channels_score=((((scale_max-scale_min) * (curr_channels-minimum_channels))/(maximum_channels-minimum_channels)) + scale_min)*lidar_sensor.default_channels_weightage

        # print("camera_sensor.security is ",camera_sensor.security*camera_sensor.default_security_weightage)
        # print("camera_sensor.accuracy is ",camera_sensor.accuracy*camera_sensor.default_accuracy_weightage)
        # print("camera_sensor.battery_consumption is ",camera_sensor.battery_consumption*camera_sensor.default_battery_consumption_weightage)
        # print("camera_sensor.detection_range is ",detect_range_score)
        # print("camera_sensor.sharpness is ",camera_sensor.sharpness * camera_sensor.default_sharpness_weightage)
        # print("camera_sensor.noise is ",camera_sensor.noise*camera_sensor.default_noise_weightage)
        # print("res is ",res_score)


        lidar_sensor.score=(lidar_sensor.security*lidar_sensor.default_security_weightage) + (lidar_sensor.accuracy*lidar_sensor.default_accuracy_weightage) + (lidar_sensor.battery_consumption*lidar_sensor.default_battery_consumption_weightage) + detect_range_score + (lidar_sensor.dust_resistance * lidar_sensor.default_dust_resistance_weightage) + channels_score + (lidar_sensor.noise*lidar_sensor.default_noise_weightage)
        
        # if lidar_sensor.score>10:
        #     print(lidar_sensor.score)




        sensor_dictionary['lidar'].append(lidar_sensor)


#add radar csv data to the dictionary 
with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/radar_data.csv','r') as f:
    w=csv.reader(f,delimiter=',')
    next(w)

    for r in w:
        radar_sensor=radar(int(r[0]),int(r[1]),int(r[2]),int(r[3]),int(r[4]),bool(r[5]))


        if len(modes_to_apply_set)!=0:
            
            weight_for_each=max_weight/len(modes_to_apply)

            temp_set_all=set(["detection_range","noise","security","accuracy","battery_consumption"])

            remaining_set = temp_set_all-modes_to_apply_set

            other_weights=0.1/len(remaining_set)

            for n in modes_to_apply_set:
                if n=="security":
                    radar_sensor.default_security_weightage=weight_for_each
                    # print("camera_sensor.default_security_weightage is ",camera_sensor.default_security_weightage)
                elif n=="accuracy":
                    radar_sensor.default_accuracy_weightage=weight_for_each
                elif n=="battery_consumption":
                    radar_sensor.default_battery_consumption_weightage=weight_for_each
            
            for n in remaining_set:
                if n=="security":
                    radar_sensor.default_security_weightage=other_weights
                elif n=="accuracy":
                    radar_sensor.default_accuracy_weightage=other_weights
                    # print("camera_sensor.default_accuracy_weightage is ",camera_sensor.default_accuracy_weightage)
                elif n=="battery_consumption":
                    radar_sensor.default_battery_consumption_weightage=other_weights
                    # print("camera_sensor.default_battery_consumption_weightage is ",camera_sensor.default_battery_consumption_weightage)
                elif n=="detection_range":
                    radar_sensor.default_detection_range_weightage=other_weights
                    # print("camera_sensor.default_detection_range_weightage is ",camera_sensor.default_detection_range_weightage)
                elif n=="noise":
                    radar_sensor.default_noise_weightage=other_weights
                    # print("camera_sensor.default_noise_weightage is ",camera_sensor.default_noise_weightage)

        if radar_sensor.radarsExist==1:
            radar_sensor.noise=2

        scale_min=1
        scale_max=10

        maximum_detection_range=600
        minimum_detection_range=10

        curr_detection_range=radar_sensor.detection_range
        detect_range_score=((((scale_max-scale_min) * (curr_detection_range-minimum_detection_range))/(maximum_detection_range-minimum_detection_range)) + scale_min)*radar_sensor.default_detection_range_weightage

        # print("camera_sensor.security is ",camera_sensor.security*camera_sensor.default_security_weightage)
        # print("camera_sensor.accuracy is ",camera_sensor.accuracy*camera_sensor.default_accuracy_weightage)
        # print("camera_sensor.battery_consumption is ",camera_sensor.battery_consumption*camera_sensor.default_battery_consumption_weightage)
        # print("camera_sensor.detection_range is ",detect_range_score)
        # print("camera_sensor.sharpness is ",camera_sensor.sharpness * camera_sensor.default_sharpness_weightage)
        # print("camera_sensor.noise is ",camera_sensor.noise*camera_sensor.default_noise_weightage)
        # print("res is ",res_score)


        radar_sensor.score=(radar_sensor.security*radar_sensor.default_security_weightage) + (radar_sensor.accuracy*radar_sensor.default_accuracy_weightage) + (radar_sensor.battery_consumption*radar_sensor.default_battery_consumption_weightage) + detect_range_score + (radar_sensor.noise*radar_sensor.default_noise_weightage)
        
        # if radar_sensor.score>10:
        #     print(radar_sensor.score)

        sensor_dictionary['radar'].append(radar_sensor)


#add gps csv data to the dictionary 
with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/gps_data.csv','r') as f:
    w=csv.reader(f,delimiter=',')
    next(w)

    for r in w:
        gps_sensor=gps(int(r[0]),int(r[1]),int(r[2]),int(r[3]))


        if len(modes_to_apply_set)!=0:
            
            weight_for_each=max_weight/len(modes_to_apply)

            temp_set_all=set(["noise","security","accuracy","battery_consumption"])

            remaining_set = temp_set_all-modes_to_apply_set

            other_weights=0.1/len(remaining_set)

            for n in modes_to_apply_set:
                if n=="security":
                    gps_sensor.default_security_weightage=weight_for_each
                    # print("camera_sensor.default_security_weightage is ",camera_sensor.default_security_weightage)
                elif n=="accuracy":
                    gps_sensor.default_accuracy_weightage=weight_for_each
                elif n=="battery_consumption":
                    gps_sensor.default_battery_consumption_weightage=weight_for_each
            
            for n in remaining_set:
                if n=="security":
                    gps_sensor.default_security_weightage=other_weights
                elif n=="accuracy":
                    gps_sensor.default_accuracy_weightage=other_weights
                    # print("camera_sensor.default_accuracy_weightage is ",camera_sensor.default_accuracy_weightage)
                elif n=="battery_consumption":
                    gps_sensor.default_battery_consumption_weightage=other_weights
                    # print("camera_sensor.default_battery_consumption_weightage is ",camera_sensor.default_battery_consumption_weightage)
                elif n=="noise":
                    gps_sensor.default_noise_weightage=other_weights
                    # print("camera_sensor.default_noise_weightage is ",camera_sensor.default_noise_weightage)

        scale_min=1
        scale_max=10

        maximum_accuracy=500
        minimum_accuracy=5

        curr_accuracy=gps_sensor.accuracy
        accuracy_score=((((scale_max-scale_min) * (curr_accuracy-minimum_accuracy))/(maximum_accuracy-minimum_accuracy)) + scale_min)*gps_sensor.default_accuracy_weightage

        # print("camera_sensor.security is ",camera_sensor.security*camera_sensor.default_security_weightage)
        # print("camera_sensor.accuracy is ",camera_sensor.accuracy*camera_sensor.default_accuracy_weightage)
        # print("camera_sensor.battery_consumption is ",camera_sensor.battery_consumption*camera_sensor.default_battery_consumption_weightage)
        # print("camera_sensor.detection_range is ",detect_range_score)
        # print("camera_sensor.sharpness is ",camera_sensor.sharpness * camera_sensor.default_sharpness_weightage)
        # print("camera_sensor.noise is ",camera_sensor.noise*camera_sensor.default_noise_weightage)
        # print("res is ",res_score)


        gps_sensor.score=(gps_sensor.security*gps_sensor.default_security_weightage) + (gps_sensor.battery_consumption*gps_sensor.default_battery_consumption_weightage) - accuracy_score + (gps_sensor.noise*gps_sensor.default_noise_weightage)
        
        # if gps_sensor.score>10:
        #     print(gps_sensor.score)

        sensor_dictionary['gps'].append(gps_sensor)

pickle.dump(sensor_dictionary,open("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/score_dictionary.p","wb"))












