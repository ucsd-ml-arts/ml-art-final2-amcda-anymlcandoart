import os
from shutil import copyfile

f= open("new2namelist.txt","w+")
os.getcwd()
directory = "./sketches/"
new_dir = "./new2/"
os.mkdir(new_dir)
if os.path.isdir(directory):
    for i, filename in enumerate(os.listdir(directory)):
        #print (filename[:-4])
        #print (str(i))
        if filename.endswith('-2.png'):
            copyfile(directory+filename, os.path.join(new_dir, filename))
            os.rename(new_dir +filename, new_dir + filename[:-6] + ".jpg")
            f.write(new_dir + str(i) + ".jpg\n")
else:
    print ("Not a directory")
