# algorand_phrase_recovery
Python code to help an Algorand (ALGO) crypto wallet holder fix a private key phrase that has limited issues

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
