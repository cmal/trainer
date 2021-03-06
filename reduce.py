#!/usr/bin/python3
import os
import os.path
import sys
from argparse import ArgumentParser
from myconfig import MyConfig
from utils import read_file


config = MyConfig()


def handleError(error):
    sys.exit(error)


def mergeSubIndex(output, path):
    for root, dirs, files in os.walk(path, topdown=True, onerror=handleError):
        for onefile in files:
            filepath = os.path.join(root, onefile)
            if onefile.endswith(config.getIndexPostfix()):
                data = read_file(filepath)
                output.writelines([data])
            else:
                print('Unexpected file:' + filepath)


def iterateSubDirectory(oldroot, newroot, level):
    #Merge the index in oldroot
    if level <= 0:
        newindex = newroot + config.getIndexPostfix()
        dirname = os.path.dirname(newindex)
        os.path.exists(dirname) or os.makedirs(dirname)
        newindexfile = open(newindex, 'a')
        mergeSubIndex(newindexfile, oldroot)
        newindexfile.close()
        return
    #Recursive into the sub directories
    for onedir in os.listdir(oldroot):
        olddir = os.path.join(oldroot, onedir)
        newdir = os.path.join(newroot, onedir)

        if not os.path.isdir(olddir):
            sys.exit('Un-expected file:' + olddir)
        else:
            iterateSubDirectory(olddir, newdir, level - 1)


if __name__ == '__main__':
    parser = ArgumentParser(description='Reduce the levels of categories.')
    parser.add_argument('--level', action='store', default=2, \
                            help='reduce to n levels of index', type=int)
    parser.add_argument('origdir', action='store', \
                            help='original index directory')
    parser.add_argument('--destdir', action='store', \
                            help='reduced index directory', \
                            default=config.getTextIndexDir())

    args = parser.parse_args()
    print(args)
    iterateSubDirectory(args.origdir, args.destdir, args.level)
    print('done')
