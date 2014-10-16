# Author: James Edwards
# Class: TGIS 501
#
# This code will do a word count in the document of the words listed. It will also 
# print out a final count for those words and for all the words in the file.
#

lab_3_text = open('E:\\TGIS_501\\Lab3\\GIS_is_the_best.txt', 'r')
file_list = lab_3_text.read()

system_count, science_count, total_words = 0, 0, 0

for word in file_list.split(' '):
    #Set up code to know what words to count    
    if word.lower() == 'systems':
            system_count = system_count + 1
    elif word.lower() == 'science':
            science_count = science_count + 1
    else:
            total_words = total_words + 1

total_words = total_words + science_count + system_count


# Prints word counts
print "system total = " + str(system_count)

print "science total = " + str(science_count)

print "Total words = " + str(total_words)

raw_input('Hit enter to end, thank you')
