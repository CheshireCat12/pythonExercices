import time
import threading
import curses

def printTime():
    stdscr = curses.initscr()
    while True:
        #print("{}\r".format(time.ctime()))
        stdscr.addstr(0,0,time.ctime())
        stdscr.refresh()
        time.sleep(1)


t = threading.Thread(target=printTime)
t.start()
