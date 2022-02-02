#! python3

# Scans a directory for files
# Prints the name of any raw files, without a compressed image files of the same name

# Delete the files with the --del argument
# Change the base path with the --path=? argument
# Change the raw file type with the --rtype=? argument
# Change the compressed file type with the --ctype=? argument

# Saves time as you can just delete badly shot compressed image files, and then remove their corresponding raw files later
import pathlib
import os
import sys

def getFilenamesFromPath(path):
    filenames = []
    for e in path.iterdir():
        filenames.append(e.name)

    return filenames

def main():
    # Default arguments
    delete = False
    path = pathlib.Path.cwd().resolve() # If no path is specified, use the current working directory
    rtype = "NEF"
    ctype = "JPG"

    for arg in sys.argv:
        # Set the delete command line argument
        if arg == "--del":
            delete = True

        # Set the base path command line argument
        if arg.startswith("--path="):
            path = arg.removeprefix("--path=")

        # Set the raw file type command line argument
        if arg.startswith("--rtype="):
            rtype = arg.removeprefix("--rtype=")

        # Set the compressed file type command line argument
        if arg.startswith("--ctype="):
            ctype = arg.removeprefix("--ctype=")

    # Check the directories to make sure they exist
    try:
        raw_file_names = getFilenamesFromPath(path / rtype)
    except FileNotFoundError:
        print("No " + rtype + " folder")
        sys.exit()

    try:
        compressed_file_names = getFilenamesFromPath(path / ctype)
    except FileNotFoundError:
        print("No " + ctype + " folder")
        sys.exit()

    if delete:
        print("Deletion started")
    else:
        print("Comparison started")

    # Loop through the files and list or delete them
    for raw_file_name in raw_file_names:
        compressed_file_equivalent = pathlib.Path(raw_file_name).stem + '.' + ctype
        if not compressed_file_equivalent in compressed_file_names:
            print(raw_file_name)
            
            if delete:
                os.remove(path / rtype / raw_file_name)

    if delete:
        print("Deletion finished")
    else:
        print("Comparison finished")

if __name__ == "__main__":
    main()