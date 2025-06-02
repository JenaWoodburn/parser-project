#simple file parsing

#print file contents
try:
    f = open("data/constituents_short.csv", "rt") 
    contents = f.read()
    print("File contents: ")
    print(contents)
    f.close()
except:
    print("\nFile does not exist\n")


#print file contents, transformed to all lowercase 
try:
    f = open("data/constituents_short.csv", "rt") 
    contents = f.read()
    print("File contents in all lowercase:")
    print(contents.lower())
    f.close()
except:
    print("\nFile does not exist\n")


#print file header, file sections using splitlines()
try:
    f = open("data/constituents_shoot.csv", "rt") 
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
    f.close()
except:
    print("\nFile does not exist\n")


#print each header element using readline()
try:
    f = open("data/constituents_short.csv", "rt") 
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
    f.close()
except:
    print("\nFile does not exist\n")






# # #using with
# # #automatically handles file closure at end
# # with open("more_names.txt") as f:
# #      content = f.read()

# # with open("names.txt", "w") as f:
# #     f.write(content)