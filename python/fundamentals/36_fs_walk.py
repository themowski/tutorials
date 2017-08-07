import os
import os.path
# import os.path actually gives us import os, so usually you'll just see import os.path

WALK_DIR_PATH = os.path.join(os.path.dirname(__file__), 'fs_test')

# os.walk recursively walks a directory (sub)tree
for dir_path, subdir_names, file_names in os.walk(WALK_DIR_PATH):
    # Note that all of the names are relative
    print "We're walking", dir_path
    print "Subdirectory names in this directory", subdir_names
    print "File names in this directory:", file_names
    for file_name in file_names:
        # Note that the names are in a platform-specific order, not necessarily alphabetic!
        # If you want that use 'for file_name in sorted(file_names)'
        file_path = os.path.join(dir_path, file_name)
        print 'File path', file_path
    print
print

# Occasionally we will want to walk a single directory and not its children.
# Then we use os.listdir:
for name in os.listdir(WALK_DIR_PATH):
    path = os.path.join(WALK_DIR_PATH, name)
    # We only get the relative name, not what it is
    if os.path.isfile(path):
        print 'File', path
    elif os.path.isdir(path):
        print 'Directory', path
    # Other kinds???
