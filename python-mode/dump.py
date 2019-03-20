# -*- mode: snippet -*-
# name: dump object
# key: dump
# --
def dump(obj):
    print ('Type = {}'.format(type(obj)))
    for attr in dir(obj):
        print("obj.%s = %s" % (attr, getattr(obj, attr)))


