'''
Created on 18 gru 2014

@author: ghalajko
'''
from collections import namedtuple
import os

svmem = namedtuple('svmem', ['total', 'used', 'free', 'percent'])

def usage_percent(used, total, _round=None):
    """Calculate percentage usage of 'used' against 'total'."""
    try:
        ret = (float(used) / float(total)) * 100
    except ZeroDivisionError:
        ret = 0
    if _round is not None:
        return round(ret, _round)
    else:
        return ret


def virtual_memory():
    memTotal = memFree = None
    with open('/proc/meminfo', 'rb') as f:
        for line in f:
            if line.startswith(b"MemTotal:"):
                memTotal = int(line.split()[1]) * 1024
            elif line.startswith(b"MemFree:"):
                memFree = int(line.split()[1]) * 1024
            if (memTotal is not None and memFree is not None):
                break

    used = memTotal - memFree
    percent = usage_percent(used, memTotal, _round=1)
    return svmem(memTotal,used,memFree,percent)

def memory_line():
    def get_dashes(perc):
        dashes = "|" * int((float(perc) / 10 * 4))
        empty_dashes = " " * (40 - len(dashes))
        return dashes, empty_dashes
    
    mem = virtual_memory()
    dashes, empty_dashes = get_dashes(mem.percent)
    return " Mem [%s%s] %5s%% %6s/%s" % (dashes, empty_dashes,mem.percent, str(int(mem.used / 1024 / 1024)) + "M",str(int(mem.total / 1024 / 1024)) + "M")

def loadavg_line():
    av1, av2, av3 = os.getloadavg()
    return " Load average: %.2f %.2f %.2f" % (av1, av2, av3)    