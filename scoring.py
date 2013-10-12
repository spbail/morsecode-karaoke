# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:10:04 2013

@author: Claudine
"""

#morse code karaoke

#string processing of user code vs correct

#create test structures

#line_corr = '.- -... -.-. -..' 
#code_user = '.- -... -.-. -..'  # correct
#code_user = '.- --.. -.-- -..'  # wrong twice
#code_user = '-. -... .-.- --.'  # wrong half
#code_user = '.. .- -. .. .-.- -..'  # more entries
#line_user = '.-.. -.-. -..'  # less entries

import numpy as np

def get_result(list_corr, list_user):
    num_user = 0
    num_corr = 0
    for (index,line_corr) in enumerate(list_corr):
        line_user = list_user[index]
#        print line_corr
#        print line_user
        letters_corr = line_corr.split(' ')
        letters_user = line_user.split(' ')
#        print letters_corr
#        print letters_user
        
        matches = np.zeros((len(letters_corr),len(letters_user)))
        
        for (x,l_corr) in enumerate(letters_corr):
            for (y,l_user) in enumerate(letters_user):
        #        print 'l_corr:{},l_user:{},match:{},match2:{}'.format(l_corr,l_user,l_corr is l_user,l_corr == l_user)
                matches[x,y] = (l_corr == l_user)
#        print matches
    
#hacky solution!    

#dim_min = int(np.size(matches,0)<np.size(matches,1))*0 + int(np.size(matches,1)<=np.size(matches,0))*1
#print dim_min
#results = np.any(matches, axis=dim_min, out=None, keepdims=False)

        results = np.any(matches, axis=1, out=None, keepdims=False)
        print results
        num_user += sum(results)
        num_corr += len(results)
#print sum(results)
#print len(results)
    perc = float(num_user)/float(num_corr)
    return perc
    
#import morse
#list_corr = [' '.join(morse.string_to_morse('Berlin')),' '.join(morse.string_to_morse('Geek')),' '.join(morse.string_to_morse('ettes'))]
#list_user = [' '.join(morse.string_to_morse('Berlon')),' '.join(morse.string_to_morse('Geek')),' '.join(morse.string_to_morse('ette'))]
#perc = get_result(list_corr, list_user)
#print perc

