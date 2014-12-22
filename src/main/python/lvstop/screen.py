'''
Created on 18 gru 2014

@author: ghalajko
'''
import curses

class Screen(object):
    '''
       Screen object
    '''
    def __init__(self):
        try:
            self.__screen = curses.initscr()
            curses.curs_set(0)
            curses.noecho()
            curses.cbreak()
            self.__dims = self.__screen.getmaxyx()
            self.__screen.keypad(1)
            self.__screen.nodelay(1)
            self.__lineno = 0
            self.__x = 0
        except:
            self.dispose() 
            raise
            
    @property
    def screen(self):
        return self.__screen
    
    @property
    def dims(self):
        return self.__dims
    
    def hline(self):
        self.__screen.hline(self.__lineno,0,curses.ACS_HLINE,self.__dims[1])
        self.__lineno += 1
        
    def print_chr(self,char):
        self.__screen.addch(self.__lineno,self.__x,char)
        self.__x +=1
    
    def print_str(self,line,highlight=False):
        try:
            if highlight:
                line += " " * (self.__dims[1] - len(line))
                self.__screen.addstr(self.__lineno, self.__x, line, curses.A_REVERSE)
            else:
                self.__screen.addstr(self.__lineno, self.__x, line, 0)
        except curses.error:
            self.__lineno = 0
            self.__screen.refresh()
            raise
        else:
            self.__x += len(line)
        
    def print_line(self,line,highlight=False):
        try:
            if highlight:
                line += " " * (self.__dims[1] - len(line))
                self.__screen.addstr(self.__lineno, self.__x, line, curses.A_REVERSE)
            else:
                self.__screen.addstr(self.__lineno, self.__x, line, 0)
        except curses.error:
            self.__lineno = 0
            self.__screen.refresh()
            raise
        else:
            self.__lineno += 1
            self.__x = 0
        
    def reset_line(self):
        self.__screen.clear()
        self.__lineno = 0
        self.__x = 0
        
    def dispose(self):
        self.__screen.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
    
    def main_loop(self,loop):
        q = -1
        while q != ord('q'):
            self.__screen.erase()
            self.reset_line()
            loop(self)
            self.__screen.refresh()
            q = self.__screen.getch()
            if q != ord(' '):
                curses.napms(100)
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.dispose()