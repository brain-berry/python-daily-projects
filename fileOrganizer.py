import os
import shutil

# change this to the folder you may want to organine
folder_path = input("Enter the folder path to organize: ")

file_types = {
    "Images": [".jpg",".jpeg",".png",".gif"],
    "Videos": [".mp4",".mkv",".avi"],
    "Documents": [".pdf",".docx",".txt"],
    "Music":[".mp3",",wav"]
}

def get_category(extension):
    for category, extensions in file_types.items():
        if extension.lower() in extensions:
            return category
    return "Others"

files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        
        category = get_category(ext)
        category_path = os.path.join(folder_path,category)
        
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            
            shutil.move(file_path,os.path.join(category_path, file))
            
print("Files organized succesfully!!!")