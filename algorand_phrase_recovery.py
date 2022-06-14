
# WHAT DOES THIS SCRIPT DO?
#
# after writing down my algorand wallet (wallet.myalgo.com) 25 phrase words,
# I wasn't able to access my wallet the next day.  I figured that I had
# either mistyped a phrase word or swapped word positions on accident.
# so, I wrote this script to try to recover my wallet.  it worked
# and recovered my wallet for me.


# TO USE THIS SCRIPT, YOU MUST:
#
# 1) INSTALL THE ALGOSDK PACKAGE!
#     more information about this package is available here:
#     https://github.com/algorand/py-algorand-sdk
#     to install the package: $ pip3 install py-algorand-sdk
#
# 2) LOAD THE WORD LIST!
#     download the sdk wordlist from here:
#     https://github.com/algorand/py-algorand-sdk/blob/develop/algosdk/wordlist.py
#     and save that file as wordlist.py in the directory that you save this script
#     because this script imports the wordlist script
#
# 3) KNOW YOUR WALLET PUBLIC ADDRESS!
#     you should have this if you sent any coins to the wallet -- look
#     at your outgoing transactions from the source where you sent from
#
# 4) HAVE YOUR PHRASE LIST OF AT LEAST 24 of 25 WORDS, WHICH YOU BELIEVE HAS AN ISSUE!
#     and the issue needs to be relatively simple: either a single spelling
#     error, a single missing word, or a single pair of swapped phrase words


import sys #to use error text in print() messages
import time #to use time.sleep()
from algosdk import account, encoding, mnemonic #must have installed the algosdk package, see above
import wordlist #must have wordlist.py in same directory; can be found in algo's sdk on github
possible_word_list = wordlist.word_list_raw().split('\n') #import 2,049 possible phrase words

#=======================
# USER DEFINED FUNCTIONS
#=======================

#take a list containing phrase words in order from word1 to word25, and convert it
# into a string of words in the same order, separated by a space
def phrase_list_to_string(phrase_list):

    #convert list to space-delimited string
    phrase_string = ' '.join(phrase_list)

    #return the word list as a string
    return phrase_string

#take a string containing phrase words in order from word1 to word25 separated by a single space,
# and convert it into a list of words in the same order
def phrase_string_to_list(phrase_string):
    
    #convert string to list using space as delimter
    phrase_list = phrase_string.split(' ')

    #return list
    return(phrase_list)

#replace a word within the phrase at a given position with a different word
# note that position 0 = word 1; position 24 = word 25; etc.
def replace_word_in_phrase_string(phrase_string, word_position, new_word):
    new_phrase_list = phrase_string_to_list(phrase_string)
    new_phrase_list[word_position] = new_word
    return phrase_list_to_string(new_phrase_list)

#compare a phrase string with a public key to see if they match
# if they match, this script will provide the correct phrase string
# and will exit.
def compare_output_to_known_pub_key(known_public_key, phrase_string):
    error_text = ''
    try:
        derived_public_key = mnemonic.to_public_key(phrase_string)
        err=0
    except:
        err=1
        error_text = sys.exc_info()[0]

    if err == 0:
        if derived_public_key == known_public_key:
            #this message only displays if correct phrase words are determined
            print('\n', '!!! MATCH !!!', '\n\n', 'CORRECT PHRASE WORDS:\n', phrase_string, '\n\n', '!!!!!!!!!!!!!')
            return 1
        else:
            print('x', error_text)
            return 0
    else:
        print('x', error_text)
        return -1

#swap two words within the phrase string
def swap_phrase_words(phrase_string, pos1, pos2):
    phrase_list = phrase_string_to_list(phrase_string)
    pos1_word = phrase_list[pos1]
    pos2_word = phrase_list[pos2]

    new_phrase_list = phrase_list
    new_phrase_list[pos2] = pos1_word
    new_phrase_list[pos1] = pos2_word

    return(phrase_list_to_string(new_phrase_list))

#fix a single misspelled word or a single missing word (all other words must be
# spelled correctly and in the correct positions)
def cycle_each_phrase_word(phrase_list, possible_word_list, known_wallet_public_key):
    for word_position in range(0, len(phrase_list)):

        print('\n\n==================')
        print(' POSITION ', str(word_position))
        print(' ORIGINAL: ', phrase_list[word_position])
        print('==================\n\n')
        time.sleep(5)

        for guess_word in possible_word_list:
            
            old_phrase = phrase_list_to_string(phrase_list)
            new_phrase = replace_word_in_phrase_string(old_phrase, word_position, guess_word)

            print('> GUESS WORD ', guess_word, \
                  ' \t@ POSITION ', str(word_position), \
                  ' \tMSG: ',
                  end=""
                  )
            if compare_output_to_known_pub_key(known_wallet_public_key, new_phrase) == 1:
                exit()

    #this message only displays if this test doesn't find the correct phrase words
    print('sorry, no luck with this test :(')        

#fix a single swapped pair (all other words must be spelled correctly and
# in the correct positions
def cycle_all_pairwise_swaps(phrase_string, known_wallet_public_key):
    for pos1 in range(0,25):
        for pos2 in range(0,25):
            new_phrase_string = swap_phrase_words(phrase_string, pos1, pos2)
            print('> POS1 ', str(pos1),
                  ' \t@ POS2 ', str(pos2),
                  ' \tMSG: ',
                  end=""
                  )
            if compare_output_to_known_pub_key(known_wallet_public_key, new_phrase_string) == 1:
                exit()

    #this message only displays if this test doesn't find the correct phrase words
    print('sorry, no luck with this test :(')



#===================
# MAIN FUNCTION
#===================

def main():

    #enter the phrase list that isn't working here in order from word #1 to #25
    phrase_list = \
                    ['ability',
                     'able',
                     'about',
                     'above',
                     'absent',
                     'absorb',
                     'abstract',
                     'absurd',
                     'abuse',
                     'access',
                     'accident',
                     'account',
                     'accuse',
                     'achieve',
                     'acid',
                     'acoustic',
                     'acquire',
                     'across',
                     'act',
                     'action',
                     'actor',
                     'actress',
                     'actual',
                     'adapt',
                     'add'
                     ]

    #====================
    #PAIRWISE SWAP CYCLE
    #====================
    known_wallet_public_key = 'ENTER YOUR PUBLIC WALLET ADDRESS HERE'

    print('FIRST TEST:\n',
          'Try all pairwise swaps across the 25 phrase words.\n',
          'There are 25 x  25 = 625 possibilities.\n',
          'This will take less than 5 minutes.',
          'Downside: Only works if there is one swapped pair in the phrase.\n\n',
          'NOTE: WrongChecksumError means words are valid but not correct for the wallet, '
          'while ValueError means a word in the phrase is not a valid word.'
          )
    time.sleep(5)

    cycle_all_pairwise_swaps(phrase_string = phrase_list_to_string(phrase_list),
                             known_wallet_public_key = known_wallet_public_key
                             )

    #====================
    #WORD RESPELL CYCLE
    #====================
    print('SECOND TEST:\n',
          'Replace each phrase word with one of the 2,049 possible words.\n',
          'There are 25 x  2,049 = 51,225 possibilities.\n',
          'This will take less than 60 minutes.',
          'Downside: Only works if one of the 25 words is misspelled.\n\n',
          'NOTE: Checksum error means words are valid but not correct for the wallet, '
          'while Valueerror means a word in the phrase is not a valid word.'
          )
    time.sleep(5)

    cycle_each_phrase_word(phrase_list = phrase_list,
                           possible_word_list = possible_word_list,
                           known_wallet_public_key = known_wallet_public_key
                           )

    #this message only displays if both tests complete without success :(
    print('sorry, no luck finding the correct phrase words with this script.  script ending. :(')

main()
