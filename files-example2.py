# open the file for reading
file = open("textfile.txt",'r')
lines = file.readlines()
for line in lines:
    print(line)
# close and release the file
file.close()
