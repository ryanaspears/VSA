import time
start_time = time.time()

list1 = [5, 6, 2, 23, 4]
sorted_list = []

while len(list1) > 0:

    lowest = min(list1)

    index = list1.index(lowest)

    sorted_list.append(lowest)

    del list1[index]


print sorted_list

print "--- %s seconds ---" % (time.time() - start_time)
