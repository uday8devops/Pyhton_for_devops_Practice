
import os
import sys

folder = input("Please enter folder paths separated spaces:")

try:
   files = os.listdir(folder)
except FileNotFoundError:
    print("Please Enter a valid folder path")
    sys.exit(1) # I want to  break excution at this point

print(f" \n ====files in folder: {folder} \n")

for i in files:
    print("-"+i)
