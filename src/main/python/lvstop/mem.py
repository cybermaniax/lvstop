'''
Created on 18 gru 2014

@author: ghalajko
'''
import os
import psutil


def memory_line():
    def get_dashes(perc):
        dashes = "|" * int((float(perc) / 10 * 4))
        empty_dashes = " " * (40 - len(dashes))
        return dashes, empty_dashes
    
    mem = psutil.virtual_memory()
    dashes, empty_dashes = get_dashes(mem.percent)
    used = mem.total - mem.available
    line = " Mem  [%s%s %5s%%] %6s/%s" % (
                                         dashes, empty_dashes,
                                         mem.percent,
                                         str(int(used / 1024 / 1024)) + "M",
                                         str(int(mem.total / 1024 / 1024)) + "M"
                                         )

    dashes, empty_dashes = get_dashes(mem.percent)
    return line

def loadavg_line():
    av1, av2, av3 = os.getloadavg()
    return " Load average: %.2f %.2f %.2f" % (av1, av2, av3)    