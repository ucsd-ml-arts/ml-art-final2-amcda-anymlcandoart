import os
from shutil import copyfile

os.getcwd()
dir_ = "./new2/"
new_dir = "./new2/"
k = 200
if os.path.isdir(dir_):
    for i, filename in enumerate(os.listdir(dir_)):
        #print (filename[:-4])
        #print (str(i))
        os.rename(dir_ +filename, dir_ + str(k) + ".jpg")
        k = k +1
else:
    print ("Not a directory")
