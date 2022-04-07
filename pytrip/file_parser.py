"""
This module contains a parser method for parsing voxelplan files.
"""


def parse_to_var(data, var, stoptag=""):
    """ Parses a variable 'var' from 'data'.

    :returns: (out,i) tuple
    out - the rest of the line with 'var' and a " " removed. If nothing is followed, then True is returned.
    i - number of lines parsed.
    """
    out = {}
    i = 0
    if type(data) is str:
        data = data.split()
    for line in data:
        if line.find(stoptag) > -1:
            break
        items = line.split()
        if items[0] in var:  # if we have found 'var' in this line..
            if len(items) > 1:
                # remove "var" from that line, and returns the rest of that line.
                out[var[items[0]]] = line.replace(items[0] + " ", "")
            else:
                # in case nothing followed var. The presences of 'var' means smth is set to True.
                out[var[items[0]]] = True
        i += 1
    return out, i
