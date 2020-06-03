import os
cwd = os.getcwd()
file = __file__
dirname_file = os.path.dirname(__file__)
dirname_cwd = os.path.dirname(os.getcwd())
basename_file = os.path.basename(__file__)
basename_cwd = os.path.basename(os.getcwd())
package = os.path.basename(os.getcwd())

print(f"cwd:{cwd}")
print(f"file:{file}")
print(f"dirname_file:{dirname_file}")
print(f"dirname_cwd:{dirname_cwd}")
print(f"basename_file:{basename_file}")
print(f"basename_cwd:{basename_cwd}")
print(f"package:{package}")

libraries = "/Volumes/HDD/Photos Library.photoslibrary"
masters_2017_path = "/Volumes/HDD/Photos Library.photoslibrary/Masters/2017/03/21/20170321-154924"
masters_2019_path = "/Volumes/HDD/Photos Library.photoslibrary/Masters/2019/09/23"
FIND_DIR="/Volumes/HDD/Photos Library.photoslibrary/Masters/2017/03/21/20170321-154924"
