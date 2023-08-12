import os, sys


# ERROR FUNCTION
def error():
    print("USAGE: python linecounter.py -e [EXTENSION] -f [FOLDER]")
    print("EXAMPLE: python linecounter.py -e py,txt -f folder01 folder02")
    sys.exit()


def lines_counter(extensions, folders):
    total_lines = 0

    # READ ALL FOLDERS
    try:
        for folder in folders:
            for file in os.listdir(folder):
                if str(os.path.splitext(file)[-1]).replace(".", "") in extensions:
                    with open(f"{folder}/{file}", "r") as f:
                        lines = len(f.readlines())
                        total_lines += lines
                        print(f"File: {folder}/{file} | Lines: {lines}")

        # SHOW TOTAL LINES OF FILES
        print(f"Total Lines: {total_lines}")
    except:
        error()


# MAIN FUNCTION
def main():
    # SET VARIABLES
    args = sys.argv 
    extensions = []
    folders = []
    lines = 0

    # CHECK COMMAND
    if args[1] != "-e" or args[3] != "-f":
        error()
   
    try:
        # GET EXTENSIONS
        for extension in args[2].split(","):
            extensions.append(extension)

        # GET FOLDERS
        for folder in range(4, len(args)):
            folders.append(sys.argv[folder])
            
        lines_counter(extensions=extensions, folders=folders)
    except:
        print("ERROR: Script can't count lines of your files.")
        error()


if __name__ == "__main__":
    main()