import os.path

order = (
    'hello_world',
    'calculator',
    'variables',
    'types',
    'lists',
    'dicts',
    'nested_data_structures',
    'if',
    'while',
    'for',
    'pass',
    'files',
    'csv_files',
    'csv_file_with_header',
    'type_conversion',
    'libraries',
    'functions',
    'function_parameters_by_reference',
    'function_calls',
    'variadic',
    'lambda',
    'debugging',
    'exceptions',
    'classes',
    'string_review',
    'string_split_1',
    'string_split_2',
    'string_join',
    'string_format',
    'string_re',
    'fs_review',
    'fs_write',
    'fs_split',
    'fs_join',
    'fs_abspath',
    'fs_walk',
    'fs_build',
    'fs_tempfile',
    'oop_intro',
    'oop_composition',
    'oop_inheritance',
    'oop_properties',
    'oop_method_override',
    'oop_protected',
)

my_dir_path = os.path.dirname(__file__)
if len(my_dir_path) == 0:
    my_dir_path = os.getcwd()

for file_name in os.listdir(my_dir_path):
    if os.path.splitext(file_name)[1] != '.py':
        continue
    elif file_name[0] == '_' or file_name[0] == '.':
        continue
    file_path = os.path.join(my_dir_path, file_name)
    file_name_split = file_name.split('_', 1)
    if len(file_name_split) == 1:
        continue
    try:
        file_number = int(file_name_split[0])
    except ValueError:
        continue
    new_file_path = os.path.join(my_dir_path, file_name_split[1])
    print file_path, 'to', new_file_path
    os.rename(file_path, new_file_path)

for file_i, file_base_name in enumerate(order):
    file_path = os.path.join(my_dir_path, file_base_name + '.py')
    assert os.path.exists(file_path), file_path
    new_file_path = os.path.join(my_dir_path, "%02u_%s.py" % (file_i+1, file_base_name))
    print file_path, 'to', new_file_path
    os.rename(file_path, new_file_path)

