# create or overwrite the file
file = open("file_to_write.txt",'w')
# write the first line. Note ‘\n’ for a newline
file.write("Text goes on Line 1\n")
file.write("Text goes on Line 2\n")
file.write("Text goes on Line 3")
# close the file and write it to the media
file.close()
