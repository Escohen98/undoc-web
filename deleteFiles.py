#Helper script to delete files on a time interval
#I don't want your dang files. Go away.
#Adapted from https://geekflare.com/python-delete-files/

# importing the required modules
import os
import shutil
import time

# main function
def main():

	# initializing the count
	deleted_files_count = 0

	# specify the path
	path = os.getcwd() + "/static/downloads/"

	# 3 hours
	days = 0.125

	# converting days to seconds
	# time.time() returns current time in seconds
    #Could change days to hours and not multiply by 24, but eh
	#seconds = time.time() - (days * 24 * 60 * 60)
    seconds = time.time() - 30 #Test on a 30 second interval
	# checking whether the file is present in path or not
	if os.path.exists(path):
		# iterating over each and every folder and file in the path
		for files in os.walk(path):
            for file in files:
    			# comparing the days & keeping dummy file 
    			if seconds >= get_file_or_folder_age(file) && file.filename != "dummy":
    				# removing the folder
    				remove_file(root_folder)
    				deleted_files_count += 1 # incrementing count
    				break
	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1 # incrementing count

	print(f"Total files deleted: {deleted_files_count}")



def remove_file(path):
	# removing the file
	if not os.remove(path):
		# success message
		print(f"{path} is removed successfully")

	else:
		# failure message
		print(f"Unable to delete the {path}")


def get_file_or_folder_age(path):
	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime
	# returning the time
	return ctime


if __name__ == '__main__':
	main()
