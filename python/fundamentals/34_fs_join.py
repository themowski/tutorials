import os.path

my_file_path = __file__
print 'My file path', my_file_path
my_dir_path, my_file_name = os.path.split(my_file_path)
my_file_base_name, my_file_ext = os.path.splitext(my_file_name)

# os.path.join is the inverse operation of os.path.split
print 'Other file path', os.path.join(my_dir_path, 'otherfile.txt')

# There is no inverse to os.path.splitext. It is guaranteed that
assert my_file_name == my_file_base_name + my_file_ext
print 'Copy file path', os.path.join(my_dir_path, my_file_base_name + '_copy' + my_file_ext)

# Don't worry about the mix of \\ and / on Windows.
# Python will do the right thing if you give it a mixed-separator path.
