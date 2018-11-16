#!/usr/bin/env python3

# This script will do the following:
# Read an input parameter with a JSON file name (for instance my_list.json)
# The JSON will be in the following format (see below)
#
#  Dictionary that will contain one nested hash and one list
#  the hash will be of pairs of names and ages (name will be the key and age will be the value)
#  the array will be a list of ages
#
# the program will go over the list of people and divide them to buckets based on their ages
# each bucket will hold all the names of the people with age between the partition key and the following partition key
# bucket  ‘20-25’ will hold a list of name that their age is between 20 and 25 (not including)
# this data will them be saved in a yaml format in a file with the same name as the input file with changed extension.

import argparse
import json

parser = argparse.ArgumentParser(description='Analyze json file')
parser.add_argument('filename', help='The file to analyze')

args = parser.parse_args()

def read_json(filename):
    with open(filename, 'r') as filename:
        return(json.load(filename))

def analyze_data(input_data):
    output_file = str(args.filename).replace("json","yml")
    buckets = input_data["buckets"]
    buckets.sort(reverse=True)

    while buckets:
        min = buckets.pop()
        if not buckets: # The list is empty since we just popped the last item
            break
        max = buckets.pop()
        find_and_print_items(input_data["ppl_ages"],min,max,output_file)
        buckets.append(max)

def find_and_print_items(dict,min,max,output_file):
    with open(output_file,'a') as filename:
        filename.write(str(min) + "-" + str(max) + ":\n")
        for name,age in dict.items():
            if (age >= min and age < max):
                filename.write("- :" + name + "\n")

def main():
    input_data = read_json(args.filename)
    analyze_data(input_data)


if __name__ == "__main__":
    # execute only if run as a script
    main()

    
