#Author: Will Peters
#Collaborators: Erin Corcoran

#This program will be used to estimate the probabilities of certain events in PS1
import numpy as np
import matplotlib.pyplot as plt
import math

#coin flips first
def coin_flips(p, n, num_trials, event):
    """Going to use this function for problem 1, in which three fair coins were
    flipped independent of one another. We are interested in the probabilities of
    certain outcomesself.
    Args:
    n-- number of coins [base case of 3]
    p-- heads probability [0.5 for fair coin]
    trial_num-- number of trials, preset at 10,000
    event-- set of outcomes we are interested in testing
    """
    #defining our outcomes of interest

    counter=0
    for _ in range(num_trials):
        seq = np.random.choice(['H','T'], p=[p,1-p],size=n)
        result= seq.tolist()
        if result in event:
            counter+=1
    print("P(event)=",counter/num_trials)
    return None


eventa=[['T','T','T'],['H','H','H']]
eventb=[['H','H','T'],['H','T','H'],['T','H','H'],['T','T','H'],['T','H','T'],['H','T','T']]
eventc=[['H','H','T'],['T','H','H'],['T','T','H'],['H','T','T']]
eventd=[['H','H','T'],['H','T','H'],['T','H','H']]
evente=[['H','H','T'],['H','T','H'],['T','H','H'],['H','H','H']]
eventf=[['H','T','H'],['T','H','T']]
#running through the events
coin_flips(0.5, 3, 10000,eventa)
coin_flips(0.5, 3, 10000,eventb)
coin_flips(0.5, 3, 10000,eventc)
coin_flips(0.5, 3, 10000,eventd)
coin_flips(0.5, 3, 10000,evente)
coin_flips(0.5, 3, 10000,eventf)


#part 2: question 3
import random
import string

def random_string(length):
    """A helper function to help us generate random strings
    Args:
    length-- number of characters we would like, the length of our string, int
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def strings(num_trials, length):
    """Going to use this function for problem 3 of the problem set, where we are
    creating 5 character strings out of the 26 lowercase letters in the english
    alphabet. We will use it to calculate the probabilities of certain events,
    given that we are allowed to repeat letters. For simplicity, this time we
    will hardcode the different events into this function instead of creating the
    possibility of feeding the events as arguments, as we did in the previous problem
    Args:
    num_trials-- trials to test this probability, set to 10000
    length-- length of the string we wish to construct
    """
    countera=0
    counterb=0
    counterc=0
    counterd=0
    eventa=['a','b','c','d','e','f','g']
    for _ in range(num_trials):
        rand_string= random_string(length)
        if (rand_string[0] in eventa)&(rand_string[1] in eventa):
            countera+=1
        if rand_string[4]=='b':
            counterb+=1
        if ((rand_string[0] in eventa)&(rand_string[1] in eventa)) | (rand_string[4]=='b'):
            counterc+=1
        if ((rand_string[0] in eventa)&(rand_string[1] in eventa)) ^ (rand_string[4]=='b'):
            counterd+=1
    print("The probability of event a =", countera/num_trials)
    print("The probability of event b =", counterb/num_trials)
    print("The probability of event c =", counterc/num_trials)
    print("The probability of event d =", counterd/num_trials)
    return None

strings(10000, 5)
