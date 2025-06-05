#simple file parsers
import os

#make a copy of a file 
try:
    filein = open("data/constituents_short.csv", "rt") 
except FileNotFoundError:
    print(f"Input file does not exist")
    exit()
except IOError as e:
    print(f"An I/O Error occurred: {e}")
    exit()
    
try:
    fileout = open("data/out/constituents_short_copy.csv", "w") 
except FileNotFoundError:
    print(f"Output file path is invalid")
    exit()
except IOError as e:
    print(f"An I/O Error occurred: {e}")
    exit()

with filein, fileout:   
    try:
        contents = filein.read()
        fileout.write(contents)
    except IOError as e:
        print(f"An error occurred: {e}")


#make a copy of a file, contents transformed to all uppercase 
filein = "data/constituents_short.csv"
fileout = "data/out/constituents_short_upper.csv"

if not os.path.exists(filein):
    print(f"Input file does not exist: {filein}")
elif not os.path.exists(os.path.dirname(fileout)):
    print(f"Output directory does not exist: {os.path.dirname(fileout)}")
else:
    try:
        with open (filein, "rt") as filein, open(fileout, "w") as fileout:
            contents = filein.read()
            fileout.write(contents.upper())
    except IOError as e:
        print(f"An error occurred: {e}")


#pretty print file contents with headers in format:
    # Symbol: A
    # Name: Agilent Technologies
    # Sector: Life Sciences Tools & Services
#creates new file
filein = "data/constituents_short.csv"
fileout = "data/out/constituents_short_pp.csv"

if not os.path.exists(filein):
    print(f"Input file does not exist: {filein}")
elif not os.path.exists(os.path.dirname(fileout)):
    print(f"Output directory does not exist {fileout}")
else:
    try:
        with open(filein, "rt") as filein, open(fileout, "w") as fileout:
            #get header elements
            header_cols = filein.readline().rsplit(",")
            col1 = header_cols[0]
            col2 = header_cols[1]
            col3 = header_cols[2].rstrip()

            # #pretty print contents
            contents = filein.readlines()
            for row in contents:
                elements = row.rsplit(",")
                fileout.write((f'{col1}: {elements[0]}\n'))
                fileout.write((f'{col2}: {elements[1]}\n'))
                #rejoin any elements split on ',' inside "", remove ""
                sector = (",".join(elements[2:])).strip('"\n')
                fileout.write((f'{col3}: {sector}\n\n'))
    except IOError as e:
        print(f"An I/O Error occurred: {e}")


#append as set of data to an existing file

# #create file by copying 'constituents_short.csv'
try:
    filein = open("data/constituents_short.csv", "rt")
except FileNotFoundError:
    print("Input file does not exist")
    exit()
except IOError as e:
    print(f"An I/O Error occurred: {e}")
    exit()

try:
    fileout = open("data/out/constituents_short_A-B.csv", "w")
except FileNotFoundError:
    print("Output directory does not exist")
    exit()
except IOError as e:
    print(f"An I/O Error occurred: {e}")
    exit()
    
with filein, fileout:
    try:
        contents = filein.read()
        fileout.write(contents)
        fileout.write("\n")
    except IOError as e:
        print(f"An I/O Error occurred: {e}")


#append all companies beginning with 'B' to file
try:
    filein = open("data/constituents.csv")
except FileNotFoundError:
    print("Input file does not exist")
    exit()
except IOError as e:
    print(f"An I/O Error occurred")
    exit()

try:
    fileout = open("data/out/constituents_short_A-B.csv", "a")
except FileNotFoundError:
    print("Output directory does not exist")
    exit()
except IOError as e:
    print(f"An I/O Error occurred")
    exit()

with filein, fileout:        
    try:
        contents = filein.readlines()
        for line in contents:
            if line.startswith("B"):
                fileout.write(line)
    except IOError as e:
        print(f"An I/O Error occurred: {e}")
