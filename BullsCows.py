# Bulls and Cows
# bullsandcows.py n k
# where n is the number of slots
# and k is the number of types of pegs.
# For example, buildandcows.py 10 4
# Examples of valid guesses would be
# abcdabcdab
# dddddddddd

import sys
import random


def playbullsandcows(numberslots, numbertypes):
    
      
    # print the possible values    
    possiblevalues = ""
    for x in range(0, numbertypes):
        possiblevalues += chr(97+x)
    print "possible values are"    
    print possiblevalues

    # print the slots
    n = 0
    string = ""
    for x in range(0,numberslots):
        if n == 10:  n -= 10
        string += str(n)
        n += 1
    print "slots are"
    print string

    # create the password
    password = ''.join(random.choice(possiblevalues) for _ in range(numberslots))
    #print "the password is (remove this later)"
    #print password
    
    # calculate how many of each letter in the password.
    passwordeachtype = [0]*numbertypes
    for x in range(0,numberslots):
        passwordeachtype[ord(password[x])-ord('a')] += 1

    #print passwordeachtype

    guesscorrect = False
    numberguesses = 1
    while not guesscorrect:
        guessvalid = False
        while not guessvalid:
            print "What is your guess?"
            guess = raw_input()
            # check the length
            guessvalid = len(guess) == len(password)
            if not guessvalid: continue
            
            # calculate the number of letters correct in any position
            guesseachtype = [0]*numbertypes
            for x in range(0,numberslots):
                index = ord(guess[x])-ord('a')
                if index < 0 or index >= numbertypes:
                    guessvalid = False
                    break
                else:
                    guesseachtype[index] += 1

        numbercorrecttype = 0
        for x in range(0,numbertypes):
            numbercorrecttype += min(guesseachtype[x], passwordeachtype[x])          
        
        # calculate the number of black pins
        blackpins = 0
        for x in range(0,numberslots):
            if guess[x] == password[x]: blackpins += 1

        # calculate the number of white pins
        whitepins = numbercorrecttype - blackpins

        if blackpins == numberslots:
            guesscorrect = True
        else:
            print blackpins, ' black, ', whitepins, ' white'
            numberguesses += 1

    print "You Won in ", numberguesses, " guesses!"




script, numberslots, numbertypes = sys.argv
playbullsandcows(int(numberslots), int(numbertypes))
