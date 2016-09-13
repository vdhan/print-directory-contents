import os
import sys


def list_directory(str_path):
    yield str_path
    if os.path.isdir(str_path):
        list_dir = os.listdir(str_path)
        for e in list_dir:
            path = os.path.join(str_path, e)
            yield from list_directory(path)


def print_directory_contents(s_path):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    if not os.path.isdir(s_path):
        raise NotADirectoryError('Not a directory')

    dirs = list_directory(s_path)
    for d in dirs:
        print(d)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_directory_contents(sys.argv[1])
    else:
        print('Missing directory')
