import csv
import math
from datetime import date
from os import remove
from time import time

from sympy import rem
import ballot as b
ballots = []
candidates = []
removedCandidates = []
with open('LargeListBallots.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        ballots.append(b.ballot(row[0], row[1], row[2], row[3]))
        for x in range(1,3):
            if row[x] not in candidates:
                candidates.append(row[x])
voteCount = len(ballots)
candWon = False
x = 0

        
def sort(e):
    return e[1]

def printw(string):
    f.write(string)
    f.write("\n")
    print(string)

f = open(str(date.today()), "x")

while not candWon:
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

    if x > 10:
        candWon = True
    x += 1

f.close()
# for c in candidates:
#     print(c)
