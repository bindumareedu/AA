import time
from decimal import *
import matplotlib.pyplot as plt

#implementing bubble sort
def bubble_sort(temp_list):
    for i in range(0,len(temp_list)-1):
        for j in range(0,len(temp_list)-i-1):
            if (temp_list[j] > temp_list[j+1]):
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    return(temp_list)

#calculating average runtime
def calruntime(temp_list):
    temp_list = [int(x) for x in temp_list]
    t1 = []
    for p in range(0,3):
        s1: decimal = time.process_time()
        bubble_sort(temp_list)
        e1: decimal = time.process_time()
        t1.append(e1-s1)
    average=round(sum(t1)/3,3)
    return average

#Main code
x = []
y = []
complete_list = []
temp_list = []
f = open("input1.txt", "r")
#Copying all the elements from file to a list
for line in f:
    complete_list.append(line.rstrip('\n').rstrip())
counter = 500
while (counter <= len(complete_list)):
    # creating list for multiples of 500 [500:10000]
    temp_list.extend(complete_list[:counter])
    y.append(calruntime(temp_list))
    temp_list.clear()
    counter=counter+500
value = 500
for i in range(0,20):
    x.append(value)
    value = value+500
plt.plot(x, y, 'xb-')
plt.ylabel("time")
plt.xlabel("input size")
plt.show()