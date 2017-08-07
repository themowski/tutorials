import os.path

order = (
    'skeleton',
    'create_table',
    'create_table_not_null',
    'create_table_fixed_width',
    'create_table_primary_key',
    'insert',
    'select',
    'select_where',
    'delete',
    'update',
    'importing_1',
    'importing_2',
    'select_aggregate_functions',
    'select_order_by_limit',
    'transactions',
    'foreign_keys',
    'select_join',
    'read_csv',
    'single_table',
    'multiple_tables',
    'queries',
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
