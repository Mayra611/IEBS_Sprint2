#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv

with open ('actividad-clase-2.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    count = 0
    count_trips = 0
    taxi_ids = []
    for row in csv_reader:
        count = count + 1 
        if count > 1 and count < 440:
            if float(row[14])> 20 and float (row[14]) < 44 and row[15] == "Credit Card":
                if row[1] not in taxi_ids:
                    count_trips = count_trips + 1
                    taxi_ids.append(row[1])
    print (count_trips)

