# Windows Lock Screen bg scraper :D
# shivankthakur

import os
import time
import shutil

#Determine Source Directory - lockscreen pics assets directory
while(True):
    username = input("Enter system username: ")

    src_dir = r"C:\Users" + '\\' + username + r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    if(os.path.isdir(src_dir)):
        print("Source directory path:", src_dir)
        break
    else:
        print("Directory does not exist! Please enter valid username")

#Read destination directory - where u want to pictures to be stored
while(True):
    dst_dir = input("Enter Destination directory path: ")

    if(os.path.isdir(dst_dir)):
        print("Destination directory path:", dst_dir)
        break
    else:
        print("Directory does not exist! Please enter valid path")

#make a new folder and append name to dst_dir
if_folder = input("Do you want a new folder?(y/n) ")
if (if_folder.lower() == 'y' or if_folder.lower() == 'yes'):
    while(True):
        folder_name = input("Enter folder name or press enter for default name: ")

        if(folder_name == ''):
            i=0
            while(os.path.exists(os.path.join(dst_dir,'New Folder'+' ('+str(i)+')'))):
                i+=1

            os.mkdir(os.path.join(dst_dir,'New Folder'+' ('+str(i)+')'))
            dst_dir = os.path.join(dst_dir,'New Folder'+' ('+str(i)+')')
            break
        else:
            #chk if folder_name already exists
            if not os.path.exists(os.path.join(dst_dir,folder_name)):
                os.mkdir(os.path.join(dst_dir,folder_name))
                dst_dir = os.path.join(dst_dir,folder_name)
                break
            else:
                print("Folder name already exists!")

# copy files from src to dst
list_dir = os.listdir(src_dir)
# print(list_dir)
for count,filename in enumerate(list_dir):
    src_file = os.path.join(src_dir,filename)
    shutil.copy(src_file,dst_dir)   #copy file into dst directory
    os.rename(os.path.join(dst_dir,filename),os.path.join(dst_dir,"pic (" + str(count) + ").jpg"))  #rename the copied file

print("All done! :D")