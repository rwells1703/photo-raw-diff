#! python3

# Scans a directory for files
# Prints the name of any NEF files, without a JPG of the same name
# Can also delete the files with the --del argument
# Change the base path with the --path= argument

# Saves time as you can just delete badly shot JPG files, and then remove their corresponding NEFs later
import pathlib
import os
import sys

def getFilenamesFromPath(path):
    filenames = []
    for e in path.iterdir():
        filenames.append(e.name)

    return filenames

def main():
    delete = False
    path = ""

    for arg in sys.argv:
        # Set the delete command line argument
        if arg == "--del":
            delete = True

        # Set the path command line argument
        if arg.startswith("--path="):
            path = arg.removeprefix("--path=")

    # If no path is specified, use the current working directory
    if path == "":
        path = pathlib.Path.cwd().resolve()

    # Check the directories to make sure they exist
    try:
        nef_filenames = getFilenamesFromPath(path / 'NEF')
    except FileNotFoundError:
        print("No NEF folder")
        sys.exit()

    try:
        jpg_filenames = getFilenamesFromPath(path / 'JPG')
    except FileNotFoundError:
        print("No JPG folder")
        sys.exit()

    # Loop through the files and list or delete them
    for nef_name in nef_filenames:
        jpg_equivalent = pathlib.Path(nef_name).stem + '.JPG'
        if not jpg_equivalent in jpg_filenames:
            print(nef_name)
            
            if delete:
                os.remove(path / 'NEF' / nef_name)

if __name__ == "__main__":
    main()
