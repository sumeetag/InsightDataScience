
# Importing all the required library to complete the challenge.
# Datatime to convert the date to miliseconds for storing chronologically by date
# heapq to maintain max heap and min heap inorder to calculate moving median

import sys
from datetime import datetime
import time
from heapq import *

# open the two output file in append mode.

medianvals_by_zip = open(sys.argv[2], "a")
medianvals_by_date = open(sys.argv[3], "a")

# create dictionary to store the zip and date data

zip_dict = {}
date_dict = {}
time_dict = {}


# I keep two heaps (or priority queues):
#
# Max-heap small has the smaller half of the numbers. and Min-heap large has the larger half of the numbers.
# This gives me direct access to the one or two middle values (they're the tops of the heaps), so getting the median takes O(1) time. And adding a number takes O(log n) time.
#
# Supporting both min- and max-heap is more or less cumbersome in python , so I simply negate the numbers in the heap in which I want the reverse of the default order.

def addNum(min_heap, max_heap, num):

    # :type num: int
    # :rtype: void

    if not max_heap or -max_heap[0] <= num:
        heappush(min_heap, num)
        if len(min_heap) - len(max_heap) > 1:
            heappush(max_heap, -heappop(min_heap))
    else:
        heappush(max_heap, -num)
        if len(max_heap) - len(min_heap) > 1:
            heappush(min_heap, -heappop(max_heap))

    return min_heap, max_heap

def findMedian(min_heap, max_heap):

    # :rtype: float

    if len(min_heap) == len(max_heap):
        return (min_heap[0] - max_heap[0]) / 2.0
    return min_heap[0] if len(min_heap) > len(max_heap) else -max_heap[0]


# read the input file itcont
with open(sys.argv[1], "r") as f:
    for line in f:
        data = line.strip().split("|")
        cmte_id = data[0]
        zip = data[10]
        date = data[13]
        amt = data[14]
        other_id = data[15]

        # if other id is not empty or cmte id is none or amount is none then that data line is invalid and skip it.
        if len(other_id) != 0 or len(cmte_id) == 0 or len(amt) == 0:
            continue

        amt = float(amt)

        # check if zip code is not none and length greater than 5 then only consider it.
        if len(zip) >= 5:

            zip = zip[:5]

            # create a key of tuple cmte_id and zip code since pair of them should be unique.

            # if the key is not present then, initialze the key with 5 items in the value.
            # value = [list of min heap, list of max heap, current running median value, number of transaction, total amount]
            if (cmte_id, zip) not in zip_dict:
                min_heap = []
                max_heap = []

                min_heap, max_heap = addNum(min_heap, max_heap, amt)
                median = findMedian(min_heap, max_heap)

                zip_dict[(cmte_id, zip)] = [min_heap, max_heap, round(median), 1, amt]

            # if key is present, then call the addnum function and retrive the new running median. Store it back in the zip code dictionary
            else:
                zip_dict[(cmte_id, zip)][0], zip_dict[(cmte_id, zip)][1] = addNum(zip_dict[(cmte_id, zip)][0], zip_dict[(cmte_id, zip)][1], amt)
                zip_dict[(cmte_id, zip)][2] = round(findMedian(zip_dict[(cmte_id, zip)][0], zip_dict[(cmte_id, zip)][1]))
                zip_dict[(cmte_id, zip)][3] += 1
                zip_dict[(cmte_id, zip)][4] += amt

            # writing the output to the zip code file as per the format
            medianvals_by_zip.write(cmte_id + "|" + zip + "|" + str(int(zip_dict[(cmte_id, zip)][2])) + "|" + str(zip_dict[(cmte_id, zip)][3]) + "|" + str(int(zip_dict[(cmte_id, zip)][4])) + "\n")


        # check if the date is valid or not. if not valid skip it.
        if len(date) != 0:

            # convert the given date into miliseconds for sorting chronologically by date
            dd = (date[:2] + "." + date[2:4] + "." + date[4:])
            a = datetime.strptime(dd, '%m.%d.%Y')
            tt = time.mktime(time.strptime(dd, '%m.%d.%Y')) * 1000

            # similiar to the zip code part.

            if (cmte_id, date) not in date_dict:
                min_heap = []
                max_heap = []

                min_heap, max_heap = addNum(min_heap, max_heap, amt)
                median = findMedian(min_heap, max_heap)

                date_dict[(cmte_id, date)] = [min_heap, max_heap, round(median), 1, amt]

            else:
                date_dict[(cmte_id, date)][0], date_dict[(cmte_id, date)][1] = addNum(date_dict[(cmte_id, date)][0], date_dict[(cmte_id, date)][1], amt)
                date_dict[(cmte_id, date)][2] = round(findMedian(date_dict[(cmte_id, date)][0], date_dict[(cmte_id, date)][1]))
                date_dict[(cmte_id, date)][3] += 1
                date_dict[(cmte_id, date)][4] += amt

            # create a new dictionary, that will store cmte_id, date and converted date.
            # this dictionary will make the sorting faster.

            if cmte_id not in time_dict:
                time_dict[cmte_id] = set()
                time_dict[cmte_id].add((tt, date))
            else:
                time_dict[cmte_id].add((tt, date))


# to sort alphabetical by recipient and then chronologically by date

# get the sorted cmte_id values.
sort_date = sorted(time_dict)

# get the sorted date values
for i in time_dict:
    temp = sorted(time_dict[i])
    time_dict[i] = temp

# based on the sorting, store the output to date file by sorting alphabetical by recipient and then chronologically by date
for i in sort_date:
    for k,j in time_dict[i]:
        medianvals_by_date.write(i + "|" + j + "|" + str(int(date_dict[(i,j)][2])) + "|" + str(date_dict[(i,j)][3]) + "|" + str(int(date_dict[(i,j)][4])) + "\n")
