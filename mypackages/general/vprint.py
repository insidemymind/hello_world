# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

def vprint(verbose=True, *arg):
    """
    usage: vprint(0, ...): do not print
           vprint(1, ...): print
    """
    if verbose:
        print ' '.join([str(i) for i in arg])
    else:
        return None
