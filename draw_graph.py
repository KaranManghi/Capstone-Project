import numpy
import matplotlib.pyplot as plt
import pickle
import random

ga_list=pickle.load(open("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/ga_graph.p","rb"))
brute_list=pickle.load(open("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/graph_brute.p","rb"))

ga_results=random.sample(ga_list,10)
brute_results=random.sample(brute_list,10)

time_list_ga=[]
score_list_ga=[]

time_list_brute=[]
score_list_brute=[]

for i in range(len(ga_results)):
    time_list_ga.append(ga_results[i][0])
    score_list_ga.append(ga_results[i][1])

for i in range(len(brute_results)):
    time_list_brute.append(brute_results[i][0])
    score_list_brute.append(brute_results[i][1])


#referred https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/

X_labels=[i+1 for i in range(len(ga_results))]

X_values_time=numpy.arange(len(X_labels))

plt.bar(X_values_time-0.2,time_list_ga,0.4,label="GA Time")
plt.bar(X_values_time+0.2,time_list_brute,0.4,label="Brute Time")

plt.xticks(X_values_time,X_labels)
plt.legend()
plt.xlabel("Runs")
plt.ylabel("Time taken in seconds")
plt.title("Genetic Algorithm vs Brute Force Time")
# plt.show()

plt.savefig("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/time.png")

plt.clf()

X_labels=[i+1 for i in range(len(ga_results))]

X_values_time=numpy.arange(len(X_labels))

plt.bar(X_values_time-0.2,score_list_ga,0.4,label="GA Score")
plt.bar(X_values_time+0.2,score_list_brute,0.4,label="Brute Score")

plt.xticks(X_values_time,X_labels)
plt.legend()
plt.xlabel("Runs")
plt.ylabel("Score achieved")
plt.title("Genetic Algorithm vs Brute Force Score")

plt.savefig("C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/score.png")

percent_sum_time=0
for i in range(len(time_list_ga)):
    percent_sum_time+=(time_list_ga[i]-time_list_brute[i])/(time_list_brute[i])

ga_time_percent=percent_sum_time/len(time_list_ga)

percent_sum_score=0
for i in range(len(score_list_ga)):
    percent_sum_score+=(score_list_brute[i]-score_list_ga[i])/(score_list_brute[i])

ga_score_percent=percent_sum_score/len(score_list_ga)

print("Time improvement: ", ga_time_percent)
print("Score less :",ga_score_percent)









