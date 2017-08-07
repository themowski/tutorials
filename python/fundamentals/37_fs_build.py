import os.path
import shutil # Various high-level file system utility functions

ROOT_DIR_PATH = os.path.join(os.path.dirname(__file__), 'fs_temp')

if os.path.exists(ROOT_DIR_PATH):
    shutil.rmtree(ROOT_DIR_PATH) # Recursively delete everything

# Create a directory
os.mkdir(ROOT_DIR_PATH)
# Create a subdirectory
os.mkdir(os.path.join(ROOT_DIR_PATH, 'temp_dir'))
# Create a file by opening and closing it
with open(os.path.join(ROOT_DIR_PATH, 'temp_file.txt'), 'w+b') as f:
    pass
# Copy a file
shutil.copyfile(
    os.path.join(ROOT_DIR_PATH, 'temp_file.txt'), # Source
    os.path.join(ROOT_DIR_PATH, 'temp_dir', 'temp_file_copy.txt') # Destination
)

print 'Listing of', ROOT_DIR_PATH
for dir_path, subdir_names, file_names in os.walk(ROOT_DIR_PATH):
    for subdir_name in subdir_names:
        print os.path.join(dir_path, subdir_name)
    for file_name in file_names:
        print os.path.join(dir_path, file_name)
print

# Rename a file
os.rename(
    os.path.join(ROOT_DIR_PATH, 'temp_file.txt'),
    os.path.join(ROOT_DIR_PATH, 'temp_file_renamed.txt')
)

# Delete a file
os.unlink(os.path.join(ROOT_DIR_PATH, 'temp_file_renamed.txt'))
os.unlink(os.path.join(ROOT_DIR_PATH, 'temp_dir', 'temp_file_copy.txt'))
# Delete a directory -- must be empty first
os.rmdir(os.path.join(ROOT_DIR_PATH, 'temp_dir'))

print 'Listing of', ROOT_DIR_PATH
for dir_path, subdir_names, file_names in os.walk(ROOT_DIR_PATH):
    for subdir_name in subdir_names:
        print os.path.join(dir_path, subdir_name)
    for file_name in file_names:
        print os.path.join(dir_path, file_name)

os.rmdir(ROOT_DIR_PATH)
