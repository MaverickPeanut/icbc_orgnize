#! /usr/bin/env python3
# -*- coding: utf8 -*-

#Version: 1.0
#Author: Ding Junying
#Function: Combine  ICBC's monthly money transfer record into one CSV file


import os
from glob import glob
import re
import sys
import csv

wait_option = True
while wait_option:
    year = input("Please type in the year(YYYY): ") #The year to be organized
    if re.match(r'^\d{4}$',year):
        wait_option = False #If year is in 4 digits, quit loop
    elif year == "q" or year == "Q":
        print("Bye.") #If year "q" or "Q" is typed, then exit program
        wait_option = False
        sys.exit()
    else:
        wait_option = True
file_name = [] #Define a list for file names 

for s in range(1,13): #Collect the file names in list: file_name
    file_name += glob("./" + year +  '%02d' % s + ".csv")

if len(file_name) == 0: #Quit if could not find matched files
    print("Could not find files mached Year:%s" % year)
    sys.exit()
else: # At least one file found
    print("Total %d files are to be combined, and they are:" % len(file_name))
    print(file_name)
    wait_option1 = True
    while wait_option1:
        combine = input("Are you going to combine? (Y/N)") 
        if combine == "Y" or combine == "y":
            #Open/Create the target CSV file, and define the writer
            combined_file =open('./2015_icbc.csv','w', newline='')
            writer = csv.writer (combined_file)
            #iterate file in the list of file_name
            for file in file_name:
                with open(file, 'r', newline='') as read_file:
                    reader = csv.reader(read_file, delimiter=' ', quotechar='|')
                    for line in reader:
                        print(line)
                #writer.writerow('a')
            combined_file.close()
            wait_option1 = False
        elif combine == "N" or combine == "n":
            sys.exit()
        else:
            print("Please type 'Y' or 'N'")    
print("Done! %s" % year)
