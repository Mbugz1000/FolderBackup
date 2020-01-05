import time
from distutils.dir_util import copy_tree
import shutil, os
from pathlib import Path
from datetime import datetime

def copy_dir(src, dst):
    dst.mkdir(parents=True, exist_ok=True)
    for item in os.listdir(src):
        s = src / item
        d = dst / item
        if s.is_dir():
            copy_dir(s, d)
        else:
            shutil.copy2(str(s), str(d))


def log_event(event):
    with open("log", "a") as text_file:
        text_file.write("\n" + event)

print('********************Folder Copier********************')

while True:
    command = input("\nCopy Files or Exit Program?")

    if command != 'exit':
        try:
            with open("folder_backup", "r") as text_file:
                folder_backups = text_file.read()

            with open("folders", "r") as text_file:
                folders = text_file.read()

            directories = folders.split('\n')
            # folder_locs =  [for dir in directories]

            for dir in directories:
                folder_name = dir.split('\\')[-1]
                copy_dir(Path(dir), Path(folder_backups+'\\'+folder_name))
                print('{}: Backed up {}'.format(datetime.now(), folder_name))

            print('Succeded!')
            print('-----------------------------------------------------------------------------------------------------------')


        except Exception as e:
            print('Unexpected Error Experienced!')
            log_event('{}: {}'.format(datetime.now(), e))
    else:
        break

print("\nExiting Program...")
time.sleep(2)
