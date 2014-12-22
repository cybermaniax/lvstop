#!/usr/bin/env python
'''
Created on 18 gru 2014

@author: ghalajko
'''


from lvstop.screen import Screen

from lvstop import lvs
from lvstop import mem
import curses

def vendpoint_line(screen,vendp):
    vep_str = " VIP: %s %s %s %s %s" % (vendp.mode,vendp.port,vendp.scheduler,vendp.persistent,vendp.persistent_timeout)
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
            
        vep_str = "{:<15}:{:<4} {:<6} {:>3} {:>5} {:>5}".format(reals._ip,reals._port,reals._forward_mode,reals._weight,reals._active_conn,reals._inact_conn)
        screen.print_line(vep_str)

def loop(screen):
    screen.reset_line()
    screen.print_line(mem.memory_line())
    screen.print_line(mem.loadavg_line())   
    screen.hline()
    # TRAFIC STATS
    for line in lvs.ip_vs_stat():
        screen.print_line(line)
    # IPVS
    screen.hline()
    ipvs = lvs.ip_vs_parse()
    for vendp in ipvs:
        vendp.sort_real_servers()
        vendpoint_line(screen,vendp)
                 
if __name__ == '__main__':
    with Screen() as scr:
        try:
            scr.main_loop(loop)
        except KeyboardInterrupt:
            pass
        except:
            raise