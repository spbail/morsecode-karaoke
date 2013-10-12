import threading as thread
import sys
import timed_input as tin
import sound_player as player
import subprocess
import pygame

current_line = ""
lines = ["....", "----", "... --", ".. -", "..-"]
result_lines = []
total_lines = len(lines)
song_length = 70.0;
line_index = 0
pygame.mixer.init()
pygame.mixer.music.load('/Users/sam/code/morsecode-karaoke/big.ogg')


def end_line():
    print " "
    return

def play_line(line_length, line):
    global line_index
    global current_line
    global result_lines

    print "%d: %s"% (line_index+1, line)
    line_index += 1
    current_line = tin.input(">> ", 5);
    result_lines.append(current_line)
    end_line()
    return

def end_game():

    print "\nDone! Analysing game performance..."
    print result_lines
    pygame.mixer.music.play()
    return


def start_game():
    song_timer = thread.Timer(song_length, end_game)
    song_timer.start()
    while line_index < total_lines:
        play_line(line_length, lines[line_index])
    return


if __name__ == "__main__":
    print "\nMorse Code Karaoke is GO!!!\n"
    #do = subprocess.Popen(['python2.7-32', 'play_sound.py start'])
    pygame.mixer.music.play()

    line_length = song_length / total_lines

    start_game()
    

