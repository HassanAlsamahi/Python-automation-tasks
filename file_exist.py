import os
import argparse

parser = argparse.ArgumentParser(description = "Checking file existence")
parser.add_argument("-f", "--file", type=str, required=True, help="Enter the name of the file")
parser.add_argument("-d", "--dir", type=str, default="y", help="If the file is in the same directory insert y, otherwise insert the directory(only)")
args = parser.parse_args()

file = args.file
dir = args.dir

if not (dir=='y'):
    os.chdir(dir)
if os.access(file, os.F_OK):
    print(f"{file} exists")
else:
    print(f"{file} doesn't exist")
