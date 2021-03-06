#!/usr/bin/python
#parsingUtils.py

def get_str(val,default):
    return default if not val else val

def get_int(s,default):
    try:
        ret = int(s)
        return ret
    except (ValueError,TypeError):
        return default

def is_number(s):
    try:
        ret = float(s)
        return True
    except ValueError:
        return None

def insert(orig, insert, pos):
    return orig[:pos]+insert+orig[pos:]