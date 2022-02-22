# Author: Ryan Ungerleider
# Date: 2/21/2022
# Name: BallotSystem

from copy import copy
import csv
import math
from os import remove
from os.path import exists
import os
import datetime as dt

#Sort Funtion to sort by % 
def sort(e):
    return e[1]

#Prints and Writes to file
def printw(string):
    f.write(string)
    f.write("\n")
    print(string)
dballots = []

running = True

#Running loop
while running:
    #Reset the Ballot import to avoid issues
    import ballot as b
    #Open File
    f = open(str(dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")
    #Setup Varibles
    filepath = f.name
    candidates = []
    removedCandidates = []
    ballots = copy(dballots)
    candWon = True
    x = 0
    #Prompt for Filename
    print("Please Enter the full File name of the Ballot Card")
    filename = input()
    #Confirm the Doc Exists
    if exists(filename):
        candWon = False
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                #Creates a list of all the ballots within file
                ballots.append(b.ballot(row[0], row[1], row[2], row[3]))
                #Create List of Unique 
                for x in range(1,3):
                    if row[x] not in candidates:
                        candidates.append(row[x])
        #Closes file
        csvfile.close
    else:
        print("Error Loading File")
    x=0
    #Main Round Loop (Will run until the winner is found)
    while not candWon and exists(filename):
        #Create Output Formatting
        printw("##################################################")
        printw("                     Vote Round " + str(x+1) + ":")

        #Setup varibles
        voteCount = 0
        lowestC = ["ph",math.inf]
        votes = []
        #Create object in the form of [Candidate name, vote count]
        for c in candidates:
            votes.append([c,0])
        #Loops through all Ballots and tallies votes
        for b in ballots:
            for v in votes:
                #Gets the first vote remaining  returns None if all votes eliminated
                if v[0] == b.GetVote(candidates):
                    #Increment candidate vote and total vote count (For avg)
                    v[1] += 1
                    voteCount += 1
        #Loop to elim candidates and check for a winner
        for v in votes:
            if v[1] == 0:
                if v[0] not in removedCandidates:
                    removedCandidates.append(v[0])
                candidates.remove(v[0])
            #Checks if player won
            if v[1]/voteCount >= .5:
                #Prints Win Message
                printw("--------------------------------------------------")
                printw((v[0] + " wins").center(50,' '))
                printw("--------------------------------------------------")
                candWon = True
            if v[1] < lowestC[1] and v[1] != 0:
                lowestC = v
        #Double Checks the lowest Candidate is a remaining candiate
        if lowestC[0] in candidates:
            #Removes candidate and adds to removedcandidates array 
            candidates.remove(lowestC[0])
            removedCandidates.append(lowestC[0])
        #Sort votes by percentage
        votes.sort(key=sort, reverse=True)
        #Print Column
        printw("  " +("Candidate").ljust(17).rjust(2) + ("Votes").rjust(9)+ ("Percent").rjust(15)) 
        #Print Stats of Election
        for v in votes:
            #Print All Stats
            printw(str(v[0]).ljust(24) + str(v[1]).ljust(12) + str(round(v[1]/voteCount*100, 3)) + "%")
        printw("")
        removed = ""
        #Sets up
        #  Removed Cadidates
        for r in removedCandidates:
            removed = removed + str(r) + ", "
        printw("Removed Candidates: " + str(removed))
        x +=1
    #Setup Replay Code
    doReplay = False
    #Clear Ballots for possible 
    ballots.clear()
    while not doReplay:
        print("Would you like to Run another Ballot Poll? Y/N")
        replay = input()
        if replay == 'y' or replay == 'Y':
            doReplay = True
        elif replay == 'N' or replay == 'X':
            running = False
            doReplay = True
    #Close File
    f.close()   
    
    #Remove File if nothing output
    if os.path.getsize(filepath) == 0:
        os.remove(filepath)
