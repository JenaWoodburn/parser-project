#simple file parsing

#print file contents
try:
    with open("data/constituents_short.csv", "rt") as f:
        contents = f.read()
        print("\nFile contents: ")
        print(contents)
        print("")
except FileNotFoundError:
    print("\nFile does not exist\n")
except IOError as e:
    print(f"An I/O error occured: {e}")


#print file contents, transformed to all lowercase 
try:
    f = open("data/constituents_short.csv", "rt") 
    contents = f.read()
    print("File contents in all lowercase:")
    print(contents.lower())
    print("")
except FileNotFoundError:
    print("\nFile does not exist\n")
except IOError as e:
    print(f"An I/O error occured: {e}")


#print file header, file sections using splitlines()
try:
    with open("data/constituents_short.csv", "rt") as f:
        contents = f.read()
        split = contents.splitlines()

        print("File header row:")
        print(f"{split[0]}\n")

        print("First 5 lines of data:")
        for line in range(1,6):
            print(split[line])

        print("")

        print("Last 5 lines of data:")
        for line in range(len(split)-5, len(split)):
            print(split[line])

        print("")
except FileNotFoundError:
    print("\nFile does not exist\n")
except IOError as e:
    print(f"An I/O error occured: {e}")


#print each header element using readline()
try:
    with open("data/constituents_short.csv", "rt") as f:
        header_row = f.readline()
        header_cols = header_row.rsplit(",")

        print("File headers are:")
        for i in range(len(header_cols)):
            print(header_cols[i])

        #print file sections using readlines()
        contents = f.readlines()
        print("First 10 lines of data:")
        for i in range(10):
            print(contents[i].strip())

        print("")

        print("Last 10 lines of data:")
        for i in range(len(contents)-10, len(contents)):
            print(contents[i].rstrip())

        print("")
except FileNotFoundError:
    print("\nFile does not exist\n")
except IOError as e:
    print(f"An I/O error occured: {e}")
