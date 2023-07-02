#Helper script to delete files on a time interval
#I don't want your dang files. Go away.
#Adapted from https://geekflare.com/python-delete-files/

import os, shutil, time

def main():
    deleted_files_count = 0
    path = os.getcwd() + "/static/downloads"

    #3 hours
    days = 0.125

    # converting days to seconds
    # time.time() is in seconds
    # Could change days to hours and not multiply by 24, but eh
    #seconds = time.time() - (days * 24 * 60 * 60)
    seconds = time.time() - 30 #Testing purposes only.

    if os.path.exists(path):
        #iterating through every file in the path
        #Idk why it has to be a nested for loop, but whatever.
        for files in os.walk(path):
            for file in files:
                #Comparing the days & keeping dummy file
                if seconds > get_file_age(file) && file.filename != "dummy":
                    remove_file(root_folder)
                    deleted_files_count += 1
                    break
    else:
        print(f'"{path}" is not found')

    print(f"Total files deleted: {deleted_files_count}")

#Deletes the given file.
#Similar to del_file in my other folder.
def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete the {path}")

#Gets how long the file has existed
def get_file_age(path):
    #Getting ctime of the file
    #Time is in seconds
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ = '__main__':
    main()
