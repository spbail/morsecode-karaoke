# non blocking input code from www.garyrobinson.net/2009/10/non-blocking-raw_input-for-python.html

import signal
#import getch
import sys
import select
#import char3
import getch_recipe as getch

line = ""

class AlarmException(Exception):
    pass

def alarm_handler(signum, frame):
    raise AlarmException

def get_line():
    global line
    line_cp = line
    line = ""
    if(line_cp == ""):
        return " "
    return line_cp

def input(prompt='', timeout=20):
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)

    try:
        sys.stdout.write(prompt)
        global line
        while 1:
            line += getch.get_char()
        signal.alarm(0)

    except AlarmException:
        pass

    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return " "