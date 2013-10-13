import tty, sys

height = 12 # at window size 52x13

slides = ['start', 'overview']

def read_slide(title):
    slide = open(title)
    content = []
    for line in slide:
        content.append(line.rstrip('\n'))

    i = 0
    while i < height:
        if i < len(content):
            print content[i]
        else:
            print " "
        i+=1

    slide.close()


def getchar():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == "__main__":
    i = 0
    run = True

    while i < len(slides) and run:
        s = slides[i]
        read_slide(s + ".txt")
        k = getchar()
        if k == 'd':
            i+=1
        elif k == 'a':
            i= i-1
        elif k == 'q':
            run = False

