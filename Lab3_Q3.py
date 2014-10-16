# Author: James Edwards
# Class: TGIS 501
#
# This code will replace words in a file. Along with create a new file that has
# the changed words in that file.
#

# This is the old file and new file path
infile = open('E:\\TGIS_501\\Lab3\\GIS_is_the_best.txt', 'r')
outfile = open('E:\\TGIS_501\\Lab3\\GIS_is_the_best_new.txt', 'w')

# What words to replace and what words to replace them with
replacements = {'Science':'Systems', 'science':'systems'}

# This is the code for replacing the words
for line in infile:
    for src, target in replacements.iteritems():
        line = line.replace(src, target)
    outfile.write(line)

# This closes the old and new path ways    
infile.close()
outfile.close()
