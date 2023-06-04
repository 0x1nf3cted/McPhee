import os
import shutil
import sys

def enumerate_files(dir):
    onlyfiles = [f for f in os.listdir(
        dir) if os.path.isfile(os.path.join(dir, f))]                #list all files inside a directory
    file_extensions = set([ex.split(".")[-1] for ex in onlyfiles])   #store all file extensions inside a list

    for f in file_extensions:
        folderpath = os.path.join(dir, f)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)                                  # create a folder if it's not done yet

    for f in onlyfiles:
        source = os.path.join(dir, f)
        paths = [dir, f.split(".")[-1], f]
        dest = os.path.join(*paths)
        try:
            shutil.move(source, dest)                                # move files into folders that have the same name as their extensions
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        if os.path.exists(directory) and os.path.isdir(directory):
             enumerate_files(directory)
        else:
            print("Error: check if the directory exists, or if it's not a file")
    else:
        print("sorry, not enough arguments")   # too lazy, will make some good error handling later
