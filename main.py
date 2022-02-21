from copy import copy
import csv
from lib2to3.pgen2.token import NEWLINE
import math
from datetime import date
from os import remove
from os.path import exists
import os
import datetime as dt




        
def sort(e):
    return e[1]

def printw(string):
    f.write(string)
    f.write("\n")
    print(string)



dballots = []
running = True
while running:
    import ballot as b
    f = open(str(dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")
    filepath = f.name
    candidates = []
    removedCandidates = []
    ballots = copy(dballots)
    candWon = True
    x = 0
    print("Please Enter the full File name of the Ballot Card")
    filename = input()
    if exists(filename):
        candWon = False
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                ballots.append(b.ballot(row[0], row[1], row[2], row[3]))
                for x in range(1,3):
                    if row[x] not in candidates:
                        candidates.append(row[x])
        csvfile.close
    else:
        print("Error Loading File")
    x=0
    while not candWon and exists(filename):
        
        printw("##################################################")
        printw("                     Vote Round " + str(x+1) + ":")
        voteCount = 0
        lowestC = ["ph",math.inf]
        votes = []
        for c in candidates:
            votes.append([c,0])
        #Loops through all Ballots
        for b in ballots:
            for v in votes:
                if v[0] == b.GetVote(candidates):
                    v[1] += 1
                    voteCount += 1
                
        for v in votes:
            if v[1] == 0:
                if v[0] not in removedCandidates:
                    removedCandidates.append(v[0])
                candidates.remove(v[0])
            if v[1]/voteCount >= .5:
                printw("--------------------------------------------------")
                printw((v[0] + " wins").center(50,' '))
                printw("--------------------------------------------------")
                candWon = True
            if v[1] < lowestC[1] and v[1] != 0:
                lowestC = v
        if lowestC[0] in candidates:
            candidates.remove(lowestC[0])
            removedCandidates.append(lowestC[0])
        votes.sort(key=sort, reverse=True)
            
        printw("  " +("Candidate").ljust(17).rjust(2) + ("Votes").rjust(9)+ ("Percent").rjust(15)) 
        for v in votes:
            
            printw(str(v[0]).ljust(24) + str(v[1]).ljust(12) + str(round(v[1]/voteCount*100, 3)) + "%")
        printw("")
        removed = ""
        for r in removedCandidates:
            removed = removed + str(r) + ", "
        printw("Removed Candidates: " + str(removed))
        x +=1
    doReplay = False
    ballots.clear()
    while not doReplay:
        print("Would you like to Run another Ballot Poll? Y/N")
        replay = input()
        if replay == 'y' or replay == 'Y':
            doReplay = True
        elif replay == 'N' or replay == 'X':
            running = False
            doReplay = True
    f.close()   
    if os.path.getsize(filepath) == 0:
        os.remove(filepath)
