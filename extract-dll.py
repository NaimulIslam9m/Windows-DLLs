import os
import shutil


target_directory = "C:\\Windows\\System32"

for root, dirs, files in os.walk(target_directory):
    for file in files:
        if file.endswith(".dll"):
            destination_directory = "C:\\Users\\[[user_name]]\\Desktop\\exported_dlls"
            source_file = os.path.join(root, file)
            shutil.copy(source_file, destination_directory)
            print(f"Copied {source_file} to {destination_directory}")
