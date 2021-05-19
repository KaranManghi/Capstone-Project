import pickle
import time
import random
import functools
import operator
from create_dictionary_of_scores_new import camera
from create_dictionary_of_scores_new import lidar
from create_dictionary_of_scores_new import gps
from create_dictionary_of_scores_new import radar

class sensor_group:
    def __init__(self,group_list):
        self.group_list=group_list
        self.score=0

        for i in range(len(group_list)):
            self.score+=group_list[i].score
        #the time complexity of this operation is O(5) as there are always 5 sensors in a group

def change_score(o):
    o.score=0

    for i in range(len(o.group_list)):
            o.score+=o.group_list[i].score
    #the time complexity for this operation is O(5) because we have only 5 sensors

def select_top_2(top_1,top_2,population):
    
    # top_1=population[0]
    # top_2=population[1]

    for i in range(2,len(population)):
        if population[i].score>top_1.score:
            temp=top_1
            top_1=population[i]
            top_2=temp
        
        elif population[i].score < top_1.score and population[i].score>top_2.score:
            top_2=population[i]
    
    return top_1,top_2
time_val=0
score_val=0
graph_collection_ga=[]
for t in range(20):
    sensor_dictionary=pickle.load(open("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/score_dictionary.p","rb"))

    result_list=[]

    for k in sensor_dictionary:
        for item in sensor_dictionary[k]:
            result_list.append(item)
    # time complexity is O(n) as there are n different sensors even though those sensors are in different dictionaries

    """
    1.) Group the sensors based on the number of sensors needed
    2.) Select the initial population(60% from the big group) and the rest goes in the lefover list
    3.) Loop :
            i.) Select the top 2 fittest and perform crossover generating 2 more groups
            ii.) Select one from the newly generated groups and randomly remove some sensors and add some from the leftover list
            iii.) If score > last score or score >second last score : continue loop else  : break loop
    """

    sensors_per_group=5

    #shuffling because the sensors of the same type are generally grouped together but we want sensors of different types in the same group
    random.shuffle(result_list)

    sensor_groups_list=[]

    # start_time=time.clock()

    curr=0
    temp=[]
    for i in range(len(result_list)):
        
        if curr<5:
            temp.append(result_list[i])
            curr+=1
        
        if curr>=5:
            sensor_groups_list.append(temp)
            curr=0
            temp=[]
    # the time complexity for this operation is O(number_of_sensors / 5)

    # print(len(sensor_groups[0]))
    # print(sensor_groups[0])

    initial_population_percentage=40

    # start_time=time.clock()
    initial_population=[]
    for i in range(0,int((initial_population_percentage/100)*len(sensor_groups_list))):
        new_group=sensor_group(sensor_groups_list[i])
        initial_population.append(new_group)
    #the time complexity of this operation is O((initial_population_percentage / 100) * len(sensor_groups_list) )

    # initial_population = sensor_groups_list[0:int(0.6*len(sensor_groups_list))]

    """
        left over population is not of type sensor group class. It is just a list of individual sensors
    """
    # left_over_population=[]
    # for i in range(int((initial_population_percentage/100)*len(sensor_groups_list)),len(sensor_groups_list)):
    #     for j in range(len(sensor_groups_list[i])):
    #         left_over_population.append(sensor_groups_list[i][j])
    # start_time=time.clock()
    left_over_population=sensor_groups_list[int((initial_population_percentage/100)*len(sensor_groups_list)):len(sensor_groups_list)]
    #Time complexity for this operation is O(n)

    # left_over_population=functools.reduce(operator.iconcat,left_over_population_groups,[])


    # sensor_groups_list[int(0.6*len(sensor_groups_list)):]

    # left_over_population=[]
    # for i in range(int(0.6*len(sensor_groups_list)),len(sensor_groups_list)):
    #     new_group=sensor_group(sensor_groups_list[i])
    #     left_over_population.append(new_group)


    last_score=0
    second_last_score=0
    curr_score=1

    score_list=[0,0]

    # print(initial_population[0][0].type)

    # initial_population.sort(key=lambda a:a.score)
    start_time=time.clock()


    # initial_population.sort(key=lambda a:-a.score)

    top_1=initial_population[0]
    top_2=initial_population[1]

    top_1,top_2=select_top_2(top_1,top_2,initial_population)
    curr_generation=0

    while curr_generation<10:
    # for c in range(1):

        # parent_1=initial_population[0]
        # parent_2=initial_population[1]

        crossover_point=random.randint(0,sensors_per_group-1)

        top_1.group_list=top_2.group_list[0:crossover_point+1] + top_1.group_list[crossover_point+1:]
        #time complexity of this operation is O(5) in our case as in a group there are only 5 sensors

        top_2.group_list=top_1.group_list[0:crossover_point+1] + top_2.group_list[crossover_point+1:]

        if len(top_1.group_list) > 5:
            print("parent 1 size error")

        if len(top_2.group_list) > 5:
            print("parent 2 size error")
        

        mutation_member=random.randint(0,1)

        if mutation_member==0:
            individual_to_mutate=top_1
        else:
            individual_to_mutate=top_2

        mutation_amount=random.randint(0,2)

        if mutation_amount!=0:
            
            #mutation_positions is a list
            mutation_positions=random.sample((0,4),mutation_amount)

            left_over_positions_x=random.sample((0,len(left_over_population)-1),mutation_amount)
            left_over_positions_y=random.sample((0,4),mutation_amount)
            
            for i in range(len(left_over_positions_x)):
                individual_to_mutate.group_list[mutation_positions[i]]=left_over_population[left_over_positions_x[i]][left_over_positions_y[i]]
            #The time complexity for this operation is O(3) because 3 is the max mutation amount
        
        change_score(top_1)
        change_score(top_2)

        # initial_population.sort(key=lambda a:-a.score)
        #Time complexity of the above operation is O(n*logn)

        top_1,top_2=select_top_2(top_1,top_2,initial_population)

        curr_score=top_1.score
        # last_score=score_list[-1]
        # second_last_score=score_list[-2]
        score_list.append(curr_score)
        curr_generation+=1
    time_val+=time.clock()-start_time
    score_val+=top_1.score
    graph_collection_ga.append((time_val,top_1.score))

# print("Task completed in " , time.clock()-start_time)
print("Average time taken to complete is ",time_val/20)
print("Average Score is ",score_val/20)
pickle.dump(graph_collection_ga,open("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/ga_graph.p","wb"))


