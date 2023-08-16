import shutil
import os
import sys
def logic(link, prev_paths):

    if link not in prev_paths:
        with open("paths.txt", "a") as file:
            file.write(link + "\n")
    
    downloads_path = r'C:\Users\simob\Downloads'
    downloads = os.listdir(downloads_path)

    timestamps = [(entry, os.path.getmtime(os.path.join(downloads_path, entry))) for entry in downloads]

    timestamps.sort(key= lambda x:x[1], reverse=True)

    most_recent_file = timestamps[0][0]
    file_path_to_download = downloads_path + '\\' + most_recent_file

    shutil.move(file_path_to_download, link)
    sys.exit()