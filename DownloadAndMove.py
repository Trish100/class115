import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Trish/Downloads"              # Add the path of you "Downloads" folder.
to_dir = "C:/Users/Trish/OneDrive/Desktop/Document_Files" #Create "Document_Files" folder in your Desktop and update the path accordingly.

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)
            if(extension in value):
                filename = os.path.basename(event.src_path)
                print("downloaded: ", filename)
                path1 = from_dir + "/" + filename
                path2 = to_dir + "/" + key
                path3 = to_dir + '/' + key + "/" + filename
                time.sleep(1)
                if(os.path.exists(path2)):
                    print("directory exists")
                    time.sleep(1)
                    if(os.path.exists(path3)):
                        print("file already exists in ", key)
                        print("renaming file" + filename)
                        newfilename = os.path.splitext(filename)[0] + str(random.randint(0,99)) + os.path.splitext(filename)[1]
                        path4 = to_dir + "/" + key + "/" + newfilename

                        print("moving" + filename)
                        shutil.move(path1,path4)
                        time.sleep(1)
                    else:
                        print("moving" + filename)
                        shutil.move(path1, path3)
                        time.sleep(1)
                else:
                    os.makedirs(path2)
                    print("moving" , filename)
                    shutil.move(path1, path3)
                    time.sleep(1)
                    
                
            
# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

