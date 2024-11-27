import os
import shutil

def organize_files_by_folder(directory):
    os.chdir(directory)

    
    for file in os.listdir():
        if os.path.isfile(file): 
            
            folder_name, _ = os.path.splitext(file)

            
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            
            shutil.move(file, os.path.join(folder_name, file))

    print("Files have been organized into folders.")


directory_path = "."
organize_files_by_folder(directory_path)
