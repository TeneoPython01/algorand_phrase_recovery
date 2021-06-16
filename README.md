<h1>algorand_phrase_recovery</h1>

<i>Python code to help an Algorand (ALGO) crypto wallet holder fix a private key phrase that has limited issues.  Instructions are included below.</i>
<br><br>

 <h3>DID THIS SCRIPT HELP YOU?</h3>

 I hope it did.  It helped me too!  If you feel inclined to tip, here is an Algo wallet address I set up specifically for tips (not necessary but certainly welcome!)
 <br>5Q2RGRRXLC3643TFP22Y5LITE5P3SPQLZO2U4KLDALLMUMZWCOEFVEKQEQ


<h3>WHY WRITE THIS SCRIPT?</h3>

 After writing down my algorand wallet (wallet.myalgo.com) 25 phrase words,
 I wasn't able to access my wallet the next day.  I figured that I had
 either mistyped a phrase word or swapped word positions on accident.
 so, I wrote this script to try to recover my wallet.
 <br>It worked
 and recovered my wallet for me.  Apparently, when I wrote down the words, I
 had switched the positions of two of them.


 <h3>THIS SCRIPT CAN:</h3>

 1) fix a single swapped pair of words in the phrase (all other words must be spelled correctly and in the correct positions)
 2) fix a single missing missing word (all other words must be spelled correctly and in the correct positions)
 3) fix a single misspelled word (all other words must be spelled correctly and in the correct positions)


<h3>INSTRUCTIONS TO USE THIS SCRIPT:</h3>

 1) INSTALL THE ALGOSDK PACKAGE!
     <br>-more information about this package is available here: https://github.com/algorand/py-algorand-sdk
     <br>-note of security -- the package referenced is from the "verified" algorand github account
     <br>-to install the package: $ pip3 install py-algorand-sdk

 2) LOAD THE WORD LIST!
     <br>-download the sdk wordlist from here: https://github.com/algorand/py-algorand-sdk/blob/develop/algosdk/wordlist.py
     <br>-save that file as wordlist.py in the directory that you save this script, because this script imports the wordlist script

 3) KNOW YOUR WALLET PUBLIC ADDRESS!
     <br>-you should have this if you sent any coins to the wallet.  look
     at your outgoing transactions from the source where you sent from.
     you will need to enter this into the appropriate hardcoded
     variable in the script.

 4) HAVE YOUR PHRASE LIST OF AT LEAST 24 of 25 WORDS, WHICH YOU BELIEVE HAS AN ISSUE!
     <br>-a single spelling error, 
     <br>-a single missing word, 
     <br>-or, a single pair of swapped phrase words.
     <br>-you will need to enter this into the appropriate hardcoded variable in the script.

<br><br><br>
<h2>GOOD LUCK!</h2>
