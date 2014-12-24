'''
Created on 18 gru 2014

@author: ghalajko
'''

def cpu_stat_proc():
    cpus = {}
    with open('/proc/stat', 'rb') as f:
        for line in f:
            if line.startswith(b"cpu"):
                sp = line.split()
                cpus[sp[0]] = float(int(sp[1])+int(sp[3]))/(int(sp[1])+int(sp[3])+int(sp[4]))
    del cpus['cpu']
    return cpus

def cpus_line():
    def get_dashes(perc):
        dashes = "|" * int((float(perc) / 10 * 4))
        empty_dashes = " " * (40 - len(dashes))
        return dashes, empty_dashes
    
    
    cpus = cpu_stat_proc()
    cpus_lines = ()
    for key,proc in cpus.items():
        dashes, empty_dashes = get_dashes(proc*100)
        l = " {:<4} [{:s}{:s}]{: .2%}".format(key.title(),dashes,empty_dashes,proc)
        cpus_lines += (l,)
    return cpus_lines


if __name__ == '__main__':
    cpus_line()
