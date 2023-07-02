#Helper script to delete files on a time interval
#I don't want your dang files. Go away.
#Adapted from https://geekflare.com/python-delete-files/

import os, shutil, time

def main():
    deleted_files_count = 0
    path = "./static/downloads/"

    # converting days to seconds
    # time.time() is in seconds
    # Could change days to hours and not multiply by 24, but eh
    seconds = time.time() - 180 # Deletes files after 30 minutes

    if os.path.exists(path):
        #iterating through every file in the path
        #Array in-case directories or other stuff.
        for file in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]:
                file_path = os.path.join(path, file)
                #Comparing the days & keeping dummy file
                if seconds > get_file_age(file_path) and not file.__contains__("dummy"):
                    remove_file(file_path)
                    deleted_files_count += 1
                    break
    else:
        print(f'"{path}" is not found')

    if (deleted_files_count > 0):
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

if __name__ == '__main__':
    print("Starting...")
    while(True): #Keeps going
        main()
        time.sleep(300) #Iterates every 5 minutes
