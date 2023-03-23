import os
import shutil
import sys

def enumerate_files(dir):
    onlyfiles = [f for f in os.listdir(
        dir) if os.path.isfile(os.path.join(dir, f))]
    file_extensions = set([ex.split(".")[-1] for ex in onlyfiles])

    for f in file_extensions:
        folderpath = os.path.join(dir, f)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)

    for f in onlyfiles:
        source = os.path.join(dir, f)
        paths = [dir, f.split(".")[-1], f]
        dest = os.path.join(*paths)
        try:
            shutil.move(source, dest)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    enumerate_files(directory)
