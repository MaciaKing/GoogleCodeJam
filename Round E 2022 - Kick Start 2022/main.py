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

    def showWinner(self):
        countB=0
        countJ=0
        for i in self.N:
            if i=='B':
                countB=countB+1
            elif i=='J':
                countJ=countJ+1
        if countB>countJ:
            print(" ****** The Winner is B")
        elif countJ>countB:
            print(" ****** The Winner is J")
        else:
            print(" ****** There is no winner")


#Algotime min max.
class Player:
    def __init__(self,name,game,label):
        self.name=name
        self.game=game
        self.label=label
        print("I'm ",name)

    #Simple movement
    def makeMovement1(self):
        idx=0
        con=True
        while idx<len(self.game.N) and con:
            if self.game.N[idx]=='V':
                if self.game.canPutValue(idx):
                    game.setNewN(idx, self.label)
                    con=False
            idx=idx+1

    #Min Max Algortihm
    def makeMovement2(self):
        None

    

if __name__ == "__main__":
    game=Game(10)
    player1=Player("BOT",game,'B')
    player2=Player("Macia",game,'J')
    for i in range(int(len(game.N)/2)):
     player1.makeMovement1()
     player2.makeMovement1()
    game.showWinner()
    print("Final State: ", game.N)