import pickle
import time
from create_dictionary_of_scores import camera
from create_dictionary_of_scores import lidar
from create_dictionary_of_scores import gps
from create_dictionary_of_scores import radar
import random

result_list=[]

sensor_dictionary=pickle.load(open("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/score_dictionary.p","rb"))

for k in sensor_dictionary:

    for item in sensor_dictionary[k]:
        result_list.append(item)
time_val=0
graph_brute=[]
for t in range(20):
    random.shuffle(result_list)
    start_time=time.clock()
    result_list.sort(key=lambda a:-a.score)

    score=0
    for i in range(0,5):
        score+=result_list[i].score
    
    time_val+=time.clock()-start_time
    graph_brute.append((time_val,score))

print("Average time taken to complete: ",time_val/20)

# print("Task completed in " , time.clock()-start_time)

print("final score is ",score)
pickle.dump(graph_brute,open("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/graph_brute.p","wb"))
