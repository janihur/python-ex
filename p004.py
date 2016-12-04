#
# Calculate MD5 checksum for a file
#

import argparse
import hashlib

def md5checksum(file_):
    hasher = hashlib.md5()
    blocksize = 65536
    
    buf = file_.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file_.read(blocksize)
    return hasher.hexdigest()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="")
    args = parser.parse_args()

    with open(args.file, mode='rb') as f:
        print(md5checksum(f))
