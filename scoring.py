# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:10:04 2013

@author: Claudine
"""

#morse code karaoke

#string processing of user code vs correct

#create test structures

code_corr = '.- -... -.-. -..' 
#code_user = '.- -... -.-. -..'  # correct
#code_user = '.- --.. -.-- -..'  # wrong twice
#code_user = '-. -... .-.- --.'  # wrong half
#code_user = '.. .- -. .. .-.- -..'  # more entries
code_user = '.-.. -.-. -..'  # less entries

import numpy as np

letters_corr = code_corr.split(' ')
letters_user = code_user.split(' ')

matches = np.zeros((len(letters_corr),len(letters_user)))

for (x,l_corr) in enumerate(letters_corr):
    for (y,l_user) in enumerate(letters_user):
#        print 'l_corr:{},l_user:{},match:{},match2:{}'.format(l_corr,l_user,l_corr is l_user,l_corr == l_user)
        matches[x,y] = (l_corr == l_user)
    
#print matches

#hacky solution!

dim_min = int(np.size(matches,0)<np.size(matches,1))*0 + int(np.size(matches,1)<=np.size(matches,0))*1
#print dim_min
results = np.any(matches, axis=dim_min, out=None, keepdims=False)
#print sum(results)
#print len(results)
perc = float(sum(results))/float(len(results))
print perc