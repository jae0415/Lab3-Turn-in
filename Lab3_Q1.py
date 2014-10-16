# Creator: James Edwards
# TGIS 501
#
# This python code will make the file names lower case. Along with changing the
# format to .txt if it is different.
#

import os

for root, dirs, files in os.walk('E:\\TGIS_501\\Lab3\\Text_Files'):
    for name in files:
        root.split(".") #splits the root a part from the period
        print (str('file_'+(os.path.join(name)[0:7]).lower())+'.txt') #Changes the format and makes it lower case

#Do not know how to replace or add a new folder with the changes

