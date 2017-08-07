import csv

# Can supply defaults for optional parameters
# csv_file_path is required, tree is not
def read_csv(csv_file_path, tree=True):
    """
    Read a CSV file.

    @param csv_file_path path to a .csv file
    @type csv_file_path str
    @param tree optional, whether to return a tree or a list of row lists
    @type tree bool
    @return a tree representing the CSV contents or a list of the CSV's rows
    """

    # ^ That is a documentation string in the standard format.
    # In the Python standard library documentation you'll also see documentation of the form
    # read_csv(csv_file_path[, tree])
    # The [] are an ancient notation indicating that something is optional.

    if tree:
        advanced_tree = {}
        with open(csv_file_path) as csv_file:
            for row_i, row in enumerate(csv.reader(csv_file)):
                if row_i == 0:
                    continue
                branch = advanced_tree
                for column in row[:-2]:
                    branch = branch.setdefault(column, {})
                branch[row[-2]] = int(row[-1])
        return advanced_tree
    else: # Return a list of rows
        with open(csv_file_path) as csv_file:
            return list(csv.reader(csv_file))

# Not legal to have required parameters after optional ones:
#def read_csv(csv_file_path='regents.csv', tree):
#    pass


# Ways of calling this function
row_tree = read_csv('regents.csv', True) # Positional, positional
row_tree = read_csv('regents.csv') # Leave off optional parameter with default, same semantics as above
row_list = read_csv('regents.csv', tree=False) # Positional, keyword
row_list = read_csv(csv_file_path='regents.csv', tree=False) # Keyword, keyword
row_list = read_csv(tree=False, csv_file_path='regents.csv') # Keywords in any order
row_tree = read_csv(csv_file_path='regents.csv') # Keyword, tree=default
# Not legal:
# read_csv(csv_file_path='regents.csv', True) # Positional after keyword
# read_csv(csv_file_path='regents.csv', TREE=False) # Keyword names must match exactly
