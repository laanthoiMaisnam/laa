import os
from string import digits

list_files= os.listdir("C:\Users\laanthoi-pc\Desktop\prank")
print(list_files)
os.chdir("C:\Users\laanthoi-pc\Desktop\prank")
for file in list_files:
    old_name=file
    print (old_name)
    new_name=old_name.lstrip(digits)
    print (new_name)
    os.rename(old_name,new_name)

