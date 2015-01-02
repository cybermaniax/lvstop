'''
Created on 18 gru 2014

@author: ghalajko
'''
import psutil
import time

__cpus_lines = ()
__last_check = None

def cpus_line():
    def get_dashes(perc):
        dashes = "|" * int((float(perc) / 10 * 4))
        empty_dashes = " " * (40 - len(dashes))
        return dashes, empty_dashes
    global __cpus_lines
    global __last_check
    
    last_check = __last_check
    
    if None == last_check or last_check+2 < time.time():
        __last_check = time.time()
        percs = psutil.cpu_percent(interval=None, percpu=True)
        cpus_lines = ()
        for cpu_num, perc in enumerate(percs):
            dashes, empty_dashes = get_dashes(perc)
            l = " Cpu{:<2}[{:s}{:s} {:>5.1f}%]".format(cpu_num,dashes,empty_dashes,perc)
            cpus_lines += (l,)
        __cpus_lines = cpus_lines
        
        
    return __cpus_lines


if __name__ == '__main__':
    cpus_line()
