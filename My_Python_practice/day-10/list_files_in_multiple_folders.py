
import os
import sys

# Prompt user to enter folder paths separated by spaces
folder_paths = input("Please enter folder paths separated spaces:").split()


# Split the input string into a list of folder paths
for folder in folder_paths:

    try:
        # List files in the current folder
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f" \n Please Enter a valid folder path. looks like the path: < {folder} > is  incorrect")
        continue # break/continue  execution at this point
    
    print(f" \n ====files in folder: {folder} \n")

    for file in files:
        print("-"+file)

"""
# Optional exceptions 

except PermissionError:
        print(f"Permission denied for folder '{folder}'.")
except Exception as e:
        print(f"An error occurred with folder '{folder}': {e}")

"""