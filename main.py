import threading as thread
import sys
import timed_input as tin
import sound_player as player
import subprocess
import pygame
import scoring
import times
import lyricsfile_to_morse as mor


current_line = ""
lines = mor.first_word_to_morse('lyrics.txt')
lines_times = times.get_times()
result_lines = []
total_lines = len(lines)
song_length = 41.0;
line_index = 0
pygame.mixer.init()
pygame.mixer.music.load('/Users/sam/code/morsecode-karaoke/big.ogg')
song_timer = thread.Timer(0, None)
play_game = True
lyrics_file = "lyrics.txt"

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
        current_line = tin.input(">> ", lines_times[line_index]);
        result_lines.append(current_line)
        end_line()

    except EOFError:
        cancel_game()

    except KeyboardInterrupt:
        cancel_game()
    except AlarmException:
        cancel_game()


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
    while line_index < total_lines and play_game == True:
        play_line(lines[line_index])
    return

def end_game():
    print "\nDone! Analysing game performance..."
    perc = scoring.get_result(correct_lines, result_lines)
    print_result(perc)
    cancel_game()
    return

def print_result(perc):
    print "Your result: %d\%" % perc

def init_song_timer(song_length):
    timer = thread.Timer(song_length, end_game)
    return timer


if __name__ == "__main__":
    print "\nMorse Code Karaoke is GO!!!\n"
    #do = subprocess.Popen(['python2.7-32', 'play_sound.py start'])
    pygame.mixer.music.play()

    start_game(song_length)
    

