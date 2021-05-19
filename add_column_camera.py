import csv
import random

with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/Capstone Presentation/camera_dataset.csv','r') as f:
    r=csv.reader(f,delimiter=',')
    # w=csv.writer(f,delimiter=',',lineterminator='\n')
    tot=[]
    temp=next(r)
    tot.append(temp)
    
    
    for row in r:
        row[8]=random.randint(1,10)
        row[9]=random.randint(1,10)
        tot.append(row)
        
        # print(row)
    # print(tot)
    
    # w.writerows(tot)

    # for r in w:
    #     r.extend(random.randint(1,10))
    #     r.extend(random.randint(1,10))
    #     w.writerow(r)

with open('C:/Users/karan/Desktop/Capstone Project Code and All/capstone-project/Capstone Presentation/camera_dataset.csv','w') as f:
    w=csv.writer(f,delimiter=',',lineterminator='\n')
    w.writerows(tot)
