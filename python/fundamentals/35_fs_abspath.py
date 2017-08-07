import os.path

# Paths can be "relative" or "absolute".
# An absolute path starts from the root of the directory tree and specifies every part of the path.
# A relative path incorporates the paths "." (shorthand for the current directory) and/or
# ".." (shorthand for the parent directory of the current directory).

print '__file__ is always an absolute path:', __file__

my_dir_abspath = os.path.split(__file__)[0]
print 'Also an absolute path, since we just split it:', my_dir_abspath
alongside_file_path = os.path.join(my_dir_abspath, 'somefile.txt')

relative_file_name = 'regents.csv'
with open(os.path.join(my_dir_path, relative_file_name)) as f:
    pass
# Same as
relative_file_name = os.path.join('.', 'regents.csv')
print 'Relative file name', relative_file_name
with open(relative_file_name) as f:
    pass

my_parent_dir_relpath = os.path.join(my_dir_abspath, '..')
print 'My parent dir relative path', my_parent_dir_relpath
my_grandparent_dir_relpath = os.path.join(my_parent_dir_relpath, '..')
# Or:
my_grandparent_dir_relpath = os.path.join(my_dir_abspath, '..', '..')
print 'My grandparent dir relative path', my_grandparent_dir_relpath

# To get an absolute path from a relative path, use os.path.abspath
my_parent_dir_abspath = os.path.abspath(my_parent_dir_relpath)
my_grandparent_dir_abspath = os.path.abspath(my_grandparent_dir_relpath)
print 'My grandparent dir absolute path', my_grandparent_dir_abspath

# To get a relative path from an absolute path, use os.path.relpath
print 'Grandparent dir relpath again', os.path.relpath(my_grandparent_dir_abspath)
# Relative to what? The default is the current working directory. (os.getcwd())
# Can specify something else:
print 'Grandparent dir relpath again from the perspective of my parent',\
    os.path.relpath(my_grandparent_dir_abspath, my_parent_dir_abspath)

