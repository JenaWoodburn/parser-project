#simple file parsers

#make a copy of a file 
try:
    with open("data/constituents_short.csv", "rt") as filein, open("data/out/constituents_short_copy.csv", "w") as fileout:
        contents = filein.read()
        fileout.write(contents)
except FileNotFoundError:
    print("File does not exist")
except IOError as e:
    print(f"An I/O Error occurred: {e}")


#make a copy of a file, contents transformed to all uppercase 
try:
    with open ("data/constituents_short.csv", "rt") as filein, open("data/out/constituents_short_upper.csv", "w") as fileout:
        contents = filein.read()
        fileout.write(contents.upper())
except FileNotFoundError:
    print("File does not exist")
except IOError as e:
    print(f"An I/O Error occurred: {e}")


#pretty print file contents with headers in format:
    # Symbol: A
    # Name: Agilent Technologies
    # Sector: Life Sciences Tools & Services
try:
    with open("data/constituents_short.csv", "rt") as filein, open("data/out/constituents_short_pp.csv", "w") as fileout:
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
except FileNotFoundError:
    print("File does not exist")
except IOError as e:
    print(f"An I/O Error occurred: {e}")