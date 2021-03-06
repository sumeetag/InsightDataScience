# Table of Contents
1. [Introduction](README.md#introduction)
2. [Run Instruction](README.md#Run-Instruction)
3. [Dependencies](README.md#Dependencies)
4. [Approach](README.md#Approach)



# Introduction
Built a model that helps identify possible donors for a variety of upcoming election campaigns. 

This model identifies which time periods are particularly lucrative so that an analyst might later correlate them to specific fundraising events.

# Run Instruction
Update the run.sh file - python [path/python file name] [input path] [output path]

python ./src/donor_insight.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

InsightDataScience~$ bash run.sh


# Dependencies

Importing all the required library to complete the challenge.

Datatime to convert the date to miliseconds for storing chronologically by date

heapq to maintain max heap and min heap inorder to calculate moving median

math library to round the median. 

import sys

from datetime import datetime

import time

import math

from heapq import *


# Approach

<h4>Finding running Median - </h4>

I keep two heaps (or priority queues):

Max-heap small has the smaller half of the numbers. and Min-heap large has the larger half of the numbers.
This gives me direct access to the one or two middle values (they're the tops of the heaps), so getting the median takes O(1) time. And adding a number takes O(log n) time.

Supporting both min- and max-heap is more or less cumbersome in python , so I simply negate the numbers in the heap in which I want the reverse of the default order.

<h4>Checking the initial condition to consider the data or not. - </h4>

If other id is not empty or cmte id is none or amount is none then that data line is invalid and skip it.

<h4>Creating the dictionary that will store the Zip code and the CMTE_ID and the corresponding running median and other terms. - </h4>

Check if zip code is not none and length greater than 5 then only consider it.

create a key of tuple cmte_id and zip code since pair of them should be unique.
If the key is not present then, initialze the key with 5 items in the value.
value = [list of min heap, list of max heap, current running median value, number of transaction, total amount]

If key is present, then call the addnum function and retrive the new running median. Store it back in the zip code dictionary

<h4>Creating the dictionary that will store the Date and the CMTE_ID and the corresponding running median and other terms. - </h4>

Check if the date is valid or not. if not valid skip it.

Convert the given date into miliseconds for sorting chronologically by date

<h4>Sort alphabetical by recipient and then chronologically by date - </h4>

Based on the sorting, store the output to date file by sorting alphabetical by recipient and then chronologically by date

