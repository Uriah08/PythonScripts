import os
import shutil

def back_up(src_dir,des_dir):
    if not os.path.exists(src_dir):
        print("Source directory does not exist")
        return

    if not os.path.exists(des_dir):
        os.makedirs(des_dir)

    for root, _, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root,file)
            des_file = os.path.join(des_dir,file)

            try:
                shutil.copy2(src_dir, des_file)
                print(f"Copied {src_file} to {des_file}")
            except Exception as e:
                print(f"Error copying {src_file} : {e}")
source = "C:\\Users\\lj\\PycharmProjects"
destination = "D:\\RealBackup"

back_up(source,destination)