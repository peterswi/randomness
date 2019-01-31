#CSCI2244 coding asignment 0
#Author: Will Peters
#Collaborators: Erin Corcoran

import numpy as np
import matplotlib.pyplot as plt
import math

#function 1: Run Lengths
def run_lengths(n, p):
    """ Return a list of the run lengths in n tosses of a coin whose heads probability is p.
    Args:
    n-- number of tosses, a positive int
    p-- heads probability for a given toss, float between 0 and 1.
    """
    seq = np.random.choice(['H','T'], p=[p, 1-p], size =n)
    runs=[]
    pointer= ''
    count=0
    for index in range(len(seq)): #for loop feels inefficient
        if index == 0:
            pointer = seq[0]
            count+=1
        else:
            if seq[index] == pointer:
                count +=1
            else:
                runs.append(count)
                count =1
                pointer = seq[index]
            if index == (len(seq)-1):
                runs.append(count)
    return runs

run_lengths(10, 0.5)

def bincalculator(n, p, max):
    counter=2
    if p>0.5:
        r=p
        while r> max:
            counter+=1
            r=r*p
    else:
        r=1-p
        while r>max:
            counter+=1
            r=r*(1-p)
    return counter

#function 2: Maximum Run lengths
def draw_hist_longest_runs(n, p, trial_num, cumulative= False):
    """Draw a histogram of the maximum run length in n tosses of a coin with a heads probability p .
    Args:
    n-- number of tosses, positive int
    p-- heads probability, a float [0,1]
    trial_num-- number of trials used to create histogram, positive int
    cumulative-- a flag to make the histogram switch between cumulative and non cumulative modes, boolean
    """
    counter=0
    results=[]
    for i in range(trial_num):
        results.append(max(run_lengths(n, p)))
        if results[i]>6:
            counter+=1

    fig = plt.figure()
    bins = np.arange(-0.5, ((bincalculator(n,p,0.00001) +1.5))) #need to play with this to make it more mutable
    plt.hist(results, bins, cumulative=cumulative, color='salmon')
    plt.title(("{:d} trials of ".format(trial_num) + "{:d} coin tosses with ".format(n) + "success probability {:}".format(p)))
    plt.xlabel("Max Streak Lengths")
    plt.ylabel("Number of occurences")
    plt.grid(axis="both", zorder=1)
    print("Percent greater than max streak length 6 is",((counter/trial_num)*100), "%")
    return None

draw_hist_longest_runs(300, 0.5, 5000)


#problem 3

def draw_hist_num_runs(n, p , trial_num, cumulative=False):
    """Draw a histogram of the number of runs in n tosses of a coin
    with heads probability p.

    Arguments:
    n-- number of tosses
    p-- probability of observing heads
    trial_num-- number of trials used to create the histogram
    cumulative-- a flag to make the histogram switch between cumulative and non cumulative modes, boolean
    """
    results = np.array([])
    for i in range(trial_num):
        results = np.append(results, run_lengths(n, p))
    results.flatten()

    fig = plt.figure()
    bins = np.arange(-0.5, (bincalculator(n, p, 0.001)+1.5)) #need to play with this to make it more mutable
    plt.hist(results, bins, cumulative=cumulative, color='cadetblue')
    plt.title(("{:d} trials of ".format(trial_num) + "{:d} coin tosses with ".format(n) + "success probability {:}".format(p)))
    plt.xlabel("Lengths of Streaks")
    plt.ylabel("Number of occurences")
    plt.grid(axis="both", zorder=1)

    return None

draw_hist_num_runs(50, 0.2, 5000)
