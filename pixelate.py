import numpy as np
from scipy.misc import imread, imsave
from sys import argv
from error import FileNotGivenError

fname_in = None
fname_out = None

try:
    args = iter(argv[1:])
    while True:
        nxt = next(args)
        if nxt == '-i':
            fname_in = next(args)
        elif nxt == '-o':
            fname_out = next(args)
        else:
            fname_in = nxt
except StopIteration:
    if fname_in is None:
        raise FileNotGivenError('I need a file name')
    elif fname_out is None:
        index = fname_in.rfind('.')
        fname_out = fname_in[:index] + '-pxl8d' + fname_in[index:]

print(fname_in)
print(fname_out)
