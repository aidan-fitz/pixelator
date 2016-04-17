from sys import argv

class FileNotGivenError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

def files():
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
    return fname_in, fname_out
