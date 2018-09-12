import time
from decimal import *
import matplotlib.pyplot as plt
#decimal.getcontext().prec = 3



def make_list(temp_list,counter):
    temp_list.extend(complete_list[:counter])
    return(temp_list)

def sort_mylist(temp_list):
    for i in range(0,len(temp_list)):
        for j in range(0,len(temp_list)-i-1):
            if (temp_list[j] > temp_list[j + 1]):
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    return(temp_list)

def calruntime(temp_list):
    temp_list = [int(x) for x in temp_list]
    t1 = []
    for p in range(0,3):
        s1: decimal = time.process_time()
        sort_mylist(temp_list)
        e1: decimal = time.process_time()
        t1.append(e1-s1)
    average=round(sum(t1)/3,3)
    return average

#Main code
x = []
y = []
complete_list = []
temp_list = []
f = open("input.txt", "r")
for line in f:
    complete_list.append(line.rstrip('\n').rstrip())
print(len(complete_list))
counter = 500
while (counter <= 10000):
    temp_list = make_list(temp_list, counter)
    #avg = calruntime(temp_list)
    y.append(calruntime(temp_list))
    temp_list.clear()
    counter=counter+500
value = 500
for i in range(0,20):
    x.append(value)
    value = value+500
plt.plot(x, y, 'xb-')
plt.show()

