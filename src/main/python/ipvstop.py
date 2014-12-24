#!/usr/bin/env python
'''
Created on 18 gru 2014

@author: ghalajko
'''


from lvstop.screen import Screen
from lvstop import loop

                 
if __name__ == '__main__':
    with Screen() as scr:
        try:
            scr.main_loop(loop)
        except KeyboardInterrupt:
            pass
        except:
            raise