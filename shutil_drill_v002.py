#Tech Academy python drill
#item 57 of 63
import shutil
import os

#shutil.move('C:/Users/Tranel/Desktop/Folder_A/randomFile_01.txt',
#            'C:/Users/Tranel/Desktop/Folder_B')
#shutil.move('C:/Users/Tranel/Desktop/Folder_A/randomFile_02.txt',
#            'C:/Users/Tranel/Desktop/Folder_B')
#shutil.move('C:/Users/Tranel/Desktop/Folder_A/randomFile_03.txt',
#            'C:/Users/Tranel/Desktop/Folder_B')
#shutil.move('C:/Users/Tranel/Desktop/Folder_A/randomFile_04.txt',
#            'C:/Users/Tranel/Desktop/Folder_B')
            
            
strtPath = raw_input('Enter start path\\folder: ')

dirs = os.listdir(strtPath)

dstPath = raw_input('Enter destination path\\folder: ')



for var in dirs:
    varN = strtPath + '\\' + var
    shutil.move(varN, dstPath)