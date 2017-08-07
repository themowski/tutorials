# Occasionally you need to store data in a temporary file,
#   such as when you're generating or downloading more data than can fit in memory.
# You may also want to create a temporary directory to e.g., keep a set of
#   downloaded files before you use them.
# Use the tempfile module for this. Do NOT use os.tmp* functions.
import os.path
import shutil
import tempfile

with tempfile.TemporaryFile() as f:
    f.write("Temporary data")
    print "Data is at", f.name
    temp_file_name = f.name
    # Implicit f.close() here deletes the file
assert not os.path.exists(temp_file_name)

# If we want some control over the name of the file:
with tempfile.NamedTemporaryFile(prefix='my_data', suffix='.txt') as f:
    f.write("Temporary data")
    print "Data is at", f.name
    # Implicit f.close() here deletes the file

temp_dir_path = tempfile.mkdtemp()
print 'Temporary directory is', temp_dir_path
assert os.path.isdir(temp_dir_path)
try:
    with open(os.path.join(temp_dir_path, 'certain_file.txt'), 'w+b') as f:
        f.write("Data")
        # Implicit f.close() here does NOT delete the file,
        # since it's a normal file, not a temporary file
finally:
    # We have to explicitly delete the temporary directory
    shutil.rmtree(temp_dir_path)
