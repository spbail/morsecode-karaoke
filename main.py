import threading as thread
import sys
import timed_input as tin

current_line = ""
#lines = ["....", "----", "... --", ".. -", "..-"]
lines = ["....", "----"]
result_lines = []
total_lines = len(lines)
song_length = 15.0;
line_index = 0

def end_line():
    print " "

def play_line(line_length, line):
    global line_index
    global current_line
    global result_lines
    
    print "%d: %s"% (line_index+1, line)
    line_index += 1
    current_line = tin.input(">> ", 5);
    result_lines.append(current_line)
    end_line()

def end_game():

    print "\nDone! Analysing game performance..."
    print result_lines

if __name__ == "__main__":
    print "\nMorse Code Karaoke is GO!!!\n"
    line_length = song_length / total_lines

    song_timer = thread.Timer(song_length, end_game)
    song_timer.start()

    while line_index < total_lines:
        play_line(line_length, lines[line_index])

