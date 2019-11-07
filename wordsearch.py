import os
import argparse

parser = argparse.ArgumentParser("description = Search for a word in a file")
parser.add_argument("-f", "--file", type=str, required=True, help="The file you want to search in it")
parser.add_argument("-w", "--word", type=str, required=True, help="The word you want to search for")
parser.add_argument("-m", "--mode", type=str, help="Insert y if you want to do full search then print the lines found")
args = parser.parse_args()

file = args.file
word_req = args.word
mode = args.mode
count = 0
file = open(file,"r")
contents = file.readlines()
lines_found = []
numbers_found = 0
for line in contents:
    count += 1
    line = line.strip("\n")
    words = line.split(" ")
    for word in words:
        if word == word_req:
            numbers_found += 1
            lines_found.append(count)
            print(f"Found the word in line {count}")
            print(f"line: {line}")
            if not mode == 'y':
                inp = input("Press n to search for the next instance, or s to stop: ")
                if inp == 's':
                    break;
print("Found the word in lines:",*lines_found)
