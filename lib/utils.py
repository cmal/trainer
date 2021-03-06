import io
import os
import json
import shutil
from myconfig import MyConfig


config = MyConfig()


#Exceptions
class EpochError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

#Utils


#File Load/Store/Length
def read_file(infile):
    with open(infile, 'r') as f:
        data = ''.join(f.readlines())
    return data


def write_file(outfile, data):
    with open(outfile, 'w') as f:
        f.writelines([data])
    return


def get_file_length(infile):
    f = open(infile, 'r')
    f.seek(0, io.SEEK_END)
    length = f.tell()
    f.close()
    return length

def copyfile(src, dst):
    print('copying from ' + src + ' to ' + dst)
    shutil.copyfile(src, dst)


#JSON Load/Store
def load_status(infile):
    data = '{}'
    if os.access(infile, os.R_OK):
        data = read_file(infile)

    return json.loads(data)


def store_status(outfile, obj):
    write_file(outfile, json.dumps(obj))
    return


def check_epoch(obj, passname):
    epochname = passname + 'Epoch'
    if not epochname in obj:
        return False
    object_epoch = int(obj[epochname])
    config_epoch = int(config.getEpochs()[epochname])
    if object_epoch > config_epoch:
        raise EpochError('Un-excepted larger epoch en-countered.\n' + \
                             'Please increace the epoch in myconfig.py\n')

    if object_epoch < config_epoch:
        return False
    if object_epoch == config_epoch:
        return True
    return None


def sign_epoch(obj, passname):
    epochname = passname + 'Epoch'
    obj[epochname] = config.getEpochs()[epochname]

#test case
if __name__ == '__main__':
    obj = load_status('/tmp/test.status')
    print(obj)
    store_status('/tmp/test.status', obj)
