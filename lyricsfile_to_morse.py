# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:34:40 2013

@author: Claudine
"""

lyrics = []

def first_word_to_morse(filename):
    import morse
    global lyrics
    
    with open(filename) as f:
        content = f.readlines()
        
    list_morse = []
    for line in content:
        lyrics.append(line)
        
        if line != '\n':
            list_words = line.split(' ')
            firstword = ''.join(l for l in list_words[0] if l.isalnum())
            #print firstword
            firstword_morse = ' '.join(morse.string_to_morse(firstword))
            #print firstword_morse
            list_morse.append(firstword_morse)

    return list_morse    

def get_lyrics():
    return lyrics

if __name__ == "__main__":
    filename = 'D:/py/morsecode_karaoke/lyrics.txt'
    this_list = first_word_to_morse(filename)
    print this_list

