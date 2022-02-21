
class ballot:
    def __init__(self, voter, vote1, vote2, vote3):
        self.voter = voter
        self.vote1 = vote1
        self.vote2 = vote2
        self.vote3 = vote3
        
    def GetVote(self, num):
        if(num==0):
            return self.vote1
        if(num==1):
            return self.vote1
        if(num==2):
            return self.vote1
        
    def GetVote(self, candidates):
        if self.vote1 in candidates: 
            return self.vote1
        if self.vote2 in candidates: 
            return self.vote2
        if self.vote3 in candidates: 
            return self.vote3
        return None