# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:10:04 2013

@author: Claudine
"""


def find_next_match(resultdict,reflist,evallist,iref,ieval):
    if iref < len(reflist) and ieval < len(evallist):
        try:
            resultdict[iref] = evallist.index(reflist[iref], ieval)
        except ValueError:
            resultdict = find_next_match(resultdict,reflist,evallist,iref+1,ieval)
        else:
            resultdict = find_next_match(resultdict,reflist,evallist,iref+1,resultdict[iref]+1)
    return resultdict

    
def find_matches(reflist,evallist):
    maxmatches = 0
    for index in xrange(len(reflist)):
        thisdict = find_next_match({},reflist,evallist,index,0)
        nummatches = len(thisdict)
        maxmatches = max([maxmatches,nummatches])
    # deduct one point if more was typed than was expected, only if a perfect match was made
    if maxmatches==len(reflist)  and len(evallist) > len(reflist):
        maxmatches += -1
    return maxmatches

        
def get_result(list_corr, list_user):
    num_user = 0
    num_corr = 0
    #print list_corr
    #print list_user
    for (index,line_corr) in enumerate(list_corr):
        line_user = list_user[index]
#        print line_corr
#        print line_user
        letters_corr = line_corr.split(' ')
        letters_user = line_user.split(' ')
#        print letters_corr
#        print letters_user
        
        num_user += find_matches(letters_corr, letters_user)
        num_corr += len(letters_corr)
    perc = float(num_user)/float(num_corr)
    return perc


if __name__ == "__main__":
#morse code karaoke

#create test structures
#line_corr = '.- -... -.-. -..' 
#code_user = '.- -... -.-. -..'  # correct
#code_user = '.- --.. -.-- -..'  # wrong twice
#code_user = '-. -... .-.- --.'  # wrong half
#code_user = '.. .- -. .. .-.- -..'  # more entries
#line_user = '.-.. -.-. -..'  # less entries

#    list_corr = ['- .... .', '-.-- --- ..- .-.', '.-- .... .- -', '.. ..-.', '.-- . ...- .', '... ---']
#    list_user = ['- . .', '-.-- ..- .-.', '.--', '..', ' ', '... ---']

    import morse
    list_corr = [' '.join(morse.string_to_morse('Berlin')),' '.join(morse.string_to_morse('Geek')),' '.join(morse.string_to_morse('ettes'))]
    list_user = [' '.join(morse.string_to_morse('Berlon')),' '.join(morse.string_to_morse('Geek')),' '.join(morse.string_to_morse('ette'))]
    perc = get_result(list_corr, list_user)
    print perc

