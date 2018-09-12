#import maxint
#from sys
#import maxint


def maxSubArraySum(a, size):
    maxsum=0
    max_so_far = maxsum - 1
    max_ending_here = 0
    startpoint = 0
    endpoint = 0
    start = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            startpoint = start
            endpoint = i

        if max_ending_here < 0:
            max_ending_here = 0
            start = i + 1

    print("Maximum contiguous sum is %d" % (max_so_far))
    for i in range(startpoint, endpoint+1):
     print(a[i])
     '''
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
'''
# Driver program to test maxSubArraySum
#a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12 ,-5 ,-22 ,15 ,-4 ,7]
maxSubArraySum(a, len(a))

#x = []
#y = []
complete_list = []
temp_list = []
f = open("input1.txt", "r")
#Copying all the elements from file to a list
for line in f:
    complete_list.append(line.rstrip('\n').rstrip())
counter = 5000
while (counter <=len(complete_list)
    temp_list.extend(complete_list[:counter])
    maxSubArraySum(temp_list,len(temp_list))

'''while (counter <= len(complete_list)):
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
'''