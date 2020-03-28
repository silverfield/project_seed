import os

# set where is the root folder of this project, relative of this file
ROOT_DIR = '../../'

# set where is the source root folder of this project, relative of ROOT
SRC_DIR = 'src'

# set where is the data folder, relative of ROOT
DATA_DIR = 'data'


def create_directories_if_necessary(path):
    """
    Given a path, creates all the directories necessary till the last '/'
    encountered. E.g.

    if '/path/to/' exists and the path argument is '/path/to/file/is/this',
    calling this would create '/path/to/file/is/'
    """

    if '/' not in path:
        return

    dir_path = path[0:path.rfind('/') + 1]

    if os.path.exists(dir_path):
        return

    os.makedirs(dir_path)


def from_root(path, create_if_needed=False):
    """
    Returns path with project root prepended
    """
    this_file_dir = os.path.realpath(os.path.dirname(__file__))
    proj_root = os.path.join(this_file_dir, ROOT_DIR)
    result_path = os.path.join(proj_root, path)

    if create_if_needed:
        create_directories_if_necessary(result_path)

    return result_path


def from_src_root(path, create_if_needed=False):
    """
    Returns path with project root prepended
    """
    return from_root(f'{SRC_DIR}/{path}', create_if_needed=create_if_needed)


def from_data_root(path, create_if_needed=False):
    """
    Returns path with data project root prepended
    """
    return from_root(f'{DATA_DIR}/{path}', create_if_needed=create_if_needed)