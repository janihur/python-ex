#
# Make sure path exists
#

import errno
import os

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

if __name__ == '__main__':
    make_sure_path_exists('/tmp/foo/bar')
