
class ballot:
    def __init__(self, voter, vote1, vote2, vote3):
        #Setup voter and each of their votes
        self.voter = voter
        self.vote1 = vote1
        self.vote2 = vote2
        self.vote3 = vote3
    
    #Returns First remaining vote or None if all empty
    def GetVote(self, candidates):
        if self.vote1 in candidates: 
            return self.vote1
        if self.vote2 in candidates: 
            return self.vote2
        if self.vote3 in candidates: 
            return self.vote3
        return None