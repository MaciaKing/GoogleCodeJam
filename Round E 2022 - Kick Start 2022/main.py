from itertools import count
import numpy as np

class Game:
    def __init__(self, ncells):
        self.N=np.full(ncells,'V')#Set all cells available
        print("Initial State: ",self.N)

    def setNewN(self, idx, label):
        self.N[idx]=label

    def isInN(self,x):
        return x>=0 and x<len(self.N)

    def isValidCell(self,idx):
        return self.N[idx]=='V'

    def canPutValue(self,idx):
        if idx==0: #limite inferior
            if self.N[idx+1]=='V':
                return True
        elif idx+1==len(self.N):#limite superior
            if self.N[idx-1]=='V':
                return True   
        #esta x enmedio
        else:
            if self.N[idx+1]=='V':
                if self.N[idx-1]=='V':
                    return True
        return False
    

#Algotime min max.
class Player:
    def __init__(self,name,game,label):
        self.name=name
        self.game=game
        self.label=label
        print("I'm ",name)

    def makeMovement(self):
        idx=-1
        for i in self.game.N:
            idx=idx+1
            if i=='V':
                if self.game.canPutValue(idx):
                    game.setNewN(idx, self.label)
        print("Final State: ",self.game.N)
    

if __name__ == "__main__":
    game=Game(11)
    player1=Player("BOT",game,'B')
    player2=Player("Macia",game,'J')
    player1.makeMovement()
    player2.makeMovement()
    #print(game.isInN(10))