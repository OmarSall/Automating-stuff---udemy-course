import os

# path = os.path.join('folder1', 'folder2', 'folder3', 'file.png')

# # print(path)
# # print(os.sep)
# print(os.getcwd())

'''
FINDING the total size of all files in the folder

'''

# totalSize = 0

# for filename in os.listdir('E:\\Python Udemy\\Automate boting stuff with Python programming course'):
#     if not os.path.isfile(os.path.join('E:\\Python Udemy\\Automate boting stuff with Python programming course')):
#         continue
#     totalSize = totalSize + os.path.getsize(os.path.join('E:\\Python Udemy\\Automate boting stuff with Python programming course'),filename)

# print(totalSize)

''' 
Storing complex data in a binary file
'''

# import shelve

# shelfFile = shelve.open('mydata')
# shelfFile['cats'] = ['Zopie', 'Kelpie', 'Diana','Roman']
# list(shelfFile.keys())

############################################

# import shutil

# shutil.copy('c:\\spam.txt', 'c:\\delicious')        #(from, to)
# shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')        #(from, to) + renaming the file
# shutil.copytree('c:\\delicious', 'c:\\delicious_backup')            #copying the entire folder

# shutil.move('c:\\spam.txt', 'c:\\deliious\\walnut')

# shutil.move('c:\\deliious\\walnut\\spam.txt', 'c:\\deliious\\walnut\\eggs.txt')     #renaming the file

#############################################3

# import os
# os.unlink('bacon.txt')          #deleting the file inside current folder

# os.rmdir('c:\\delicious')       #removing a folder in the string - FOLDER MUST BE EMPTY!!!!

# import shutil

# shutil.rmtree('c:\\delicious')          # removing the folder with all the content inside

''' 
DRY RUN OF THE PROGRAM - for preventing bugs
'''

# import os

# os.chdir('C:\\Users\\Omar\\Desktop')

# for filename in os.listdir():
#     if filename.endswith('.txt'):
#         # os.unlink(filename)           #!!!!BEFORE deleting check if we have the desired output!!!!
#         print(filename)

# ####################################

# import send2trash

# send2trash.send2trash('C:\\Users\\Omar\\Desktop\\AI images\\creation.jpg')      #sends the file to trash bin

# import os

# for folderName,subfolders, filenames in os.walk('C:\\installs'):
#     print('The folder is ' + folderName)
#     print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
#     print('The filenames in ' + folderName + ' are: ' + str(filenames))
#     print()

#     for subfolder in filenames:
#         if file.endswith('.py'):
#             shutil.copy(os.join(folderName, file) + os.join(folderName, file + '.backup')))