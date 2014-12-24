#!/usr/bin/env python
from lvstop.cpu import cpus_line

__author__ = "Grzegorz Halajko'"
__version__ = "0.1.0"
version_info = tuple([int(num) for num in __version__.split('.')])


__all__ = ["version_info", "__version__"]


import os
import sys

if os.name != 'posix':
    sys.exit('platform not supported')

from lvstop import (lvs,mem,cpu)
import curses

def vendpoint_line(screen,vendp):
    vep_str = ' VIP: {:<3s} {:<20s} {:<5s} {:s} {:s}'.format(vendp.mode,vendp.port,vendp.scheduler,vendp.persistent,vendp.persistent_timeout)
    screen.print_line(vep_str)
    if 0 >= len(vendp.real_servers):
        return
    last = vendp.real_servers[-1]
    for reals in vendp.real_servers:
        screen.print_str('  ')
        if last == reals:
            screen.print_chr(curses.ACS_LLCORNER)
            screen.print_chr(curses.ACS_HLINE)
        else:
            screen.print_chr(curses.ACS_LTEE)
            screen.print_chr(curses.ACS_HLINE) 
            
        vep_str = '{:<15}:{:<4} {:<6} {:>3} {:>5} {:>5}'.format(reals._ip,reals._port,reals._forward_mode,reals._weight,reals._active_conn,reals._inact_conn)
        screen.print_line(vep_str)

def loop(screen):
    screen.reset_line()
    # START CPU
    cpus_line = cpu.cpus_line()
    for cpuline in cpus_line:
        screen.print_line(cpuline)
    # END CPU
    screen.print_line(mem.memory_line())
    screen.print_line(mem.loadavg_line())   
    screen.hline()
    # START TRAFIC STATS
    for line in lvs.ip_vs_stat():
        screen.print_line(line)
    # END TRAFIC STATS
    
    # START IPvS
    screen.hline()
    ipvs = lvs.ip_vs_parse()
    for vendp in ipvs:
        vendp.sort_real_servers()
    # END IPvS
        vendpoint_line(screen,vendp)    