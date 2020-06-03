import glob
import os

import utils

download_dir = '/tmp/wget'

print('--------------- glob -----------------')
os.chdir(download_dir)
print('--- glob.glob("*.htm*"): ', glob.glob("*.htm*"))
for file in glob.glob("*.htm*"):
    print('-- file in glob.glob("*.htm*"): ', file)

print('--------------- listdir -----------------')
for file in os.listdir(download_dir):
    if 'htm' in file:
        print("-- if 'htm' in file: ", os.path.join(download_dir, file))

    if file.endswith(".htm*"):
        print('-- file.endswith(".htm*"): ', os.path.join(download_dir, file))

print('--------------- walk -----------------')
for root, dirs, files in os.walk(download_dir):
    print('--- root: ', root)
    print('--- dirs: ', dirs)
    print('--- files: ', files)

    for file in files:
        if 'htm' in file:
            print("-- if 'htm' in file: ", os.path.join(root, file))
        if file.endswith(".htm*"):
            print('-- file.endswith(".htm*"): ', os.path.join(root, file))

        with open(file, 'r') as html:
            urls = utils.Client.parse(download_dir, html)

        try:
            html = open(file, "r")
            urls = utils.Client.parse(download_dir, html)
        except FileNotFoundError:
            raise
        finally:
            html.close()

