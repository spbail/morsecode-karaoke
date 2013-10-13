import threading as thread
import sys
import timed_input as tin
import subprocess
import pygame
import scoring
import times
import lyricsfile_to_morse as mor
import time

current_line = ""
lines = mor.first_word_to_morse('lyrics.txt')
lines_times = times.get_times()
result_lines = []
total_lines = len(lines)
first_bleep = lines_times[0]
song_length = lines_times[total_lines-1] + 10;
line_index = 0
pygame.mixer.init()
pygame.mixer.music.load('/Users/sam/code/morsecode-karaoke/big.ogg')
song_timer = thread.Timer(0, None)
play_game = True
lyrics_file = "lyrics.txt"
play_line = False

def end_line():
    global line_index
    line_index += 1

    print " "
    return

def play_line(line):
    global current_line
    global result_lines
    global lines_times

    print "\n%d: %s"% (line_index+1, line)
    try: 
        tin.input(">> ", get_line_time());
        current_line = tin.get_line()
        #print "current line: ", current_line
        result_lines.append(current_line)
        end_line()
    except EOFError:
        cancel_game()

    except KeyboardInterrupt:
        cancel_game()


def get_line_time():
    line_time = lines_times[line_index+1] - lines_times[line_index]
    return line_time

def cancel_game():
    global play_game
    play_game = False
    global song_timer
    song_timer.cancel()
    pygame.mixer.music.stop()

def start_game(song_length):
    global song_timer
    song_timer = init_song_timer(song_length)
    song_timer.start()

    # don't do anything for lines_times[0] seconds
    time.sleep(lines_times[0]-1)
    print "\nMorse Code Karaoke is GO!!!\n"

    while line_index < total_lines and play_game == True:
        play_line(lines[line_index])
    return

def end_game():
    print "\nDone! Analysing game performance..."
    perc = scoring.get_result(lines, result_lines)
    print_result(perc)

    print_funsies()
    time.sleep(20)

    cancel_game()

    return

def print_result(perc):
    print "Your result: %d per cent" % perc

def init_song_timer(song_length):
    timer = thread.Timer(song_length, end_game)
    return timer


def print_funsies():
    print """
    (._.)
    <) )J
    / \\
    """
    time.sleep(1)
    print """
    ( ._.)
    \( (>
    / \\
    """
    time.sleep(1)
    print """
    (._.)
    <) )J
    / \\
    """
    time.sleep(1)
    print """
    ( ._.)
    \( (>
    / \\

    """

    

if __name__ == "__main__":
    #do = subprocess.Popen(['python2.7-32', 'play_sound.py start'])
    print "\nWelcome to Morse Code Karaoke... GET READY!!!\n"

    pygame.mixer.music.play()

    start_game(song_length)
    

