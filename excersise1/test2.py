fh = open("d:/laa.txt", "r")
print (fh.read())
fh = open("d:/laa.txt", "w")
lines= ["a line of text", "another line of text", "a third line"]
fh.writelines(lines)
fh.close()



