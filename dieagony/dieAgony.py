#!/usr/bin/env python
import copy

class Die:
    def __init__(self): 
        self.faces = [None,None,None,None,None,None] #init as None before faces are known
        self.score = 0
        self.coord = [0,0]
        self.path = [] #append path through board
        self.coords = [[0,0]]
        self.allFaces = [[None,None,None,None,None,None]]
        #default faces is one is up, two is front

        #faces take the form, §

    def move(self,direction): #direction can take form f,b,l,r -> will return the faces
        if direction == "f":
            self.faces = [self.faces[1],
                        self.faces[5],
                        self.faces[2],
                        self.faces[3],
                        self.faces[0],
                        self.faces[4]]
            
            self.coord[0] += 1

        if direction == "b":
            for i in range(3): #backwards is forwards 3x
                self.faces = [self.faces[1],
                        self.faces[5],
                        self.faces[2],
                        self.faces[3],
                        self.faces[0],
                        self.faces[4]]

            self.coord[0] -= 1

        if direction == "l":
            self.faces = [self.faces[3],
                        self.faces[1],
                        self.faces[0],
                        self.faces[5],
                        self.faces[4],
                        self.faces[2]]
            
            self.coord[1] -= 1

        if direction == "r":
            for i in range(3): #right is left 3x
                self.faces = [self.faces[3],
                        self.faces[1],
                        self.faces[0],
                        self.faces[5],
                        self.faces[4],
                        self.faces[2]]

            self.coord[1] += 1
            
        
        self.path.append(direction) #add to the path the direction ta

        return self.faces
    
    def getTop(self): 
        return self.faces[0]
    
    def getMove(self):
        return len(self.path) + 1
    
    def getScore(self):
        return self.score
    
    def getCoord(self):
        return self.coord
    
    def setTop(self,value):
        self.faces[0] = value

    def getState(self):
        return (vars(self))
    
    

            

class Game:
    def __init__(self):
        self.board = [[0,77,32,403,337,452], #reflect the board along y = 0 to visually see board
                 [5,23,-4,592,445,620],
                 [-7,2,357,452,317,395],
                 [186,42,195,704,452,228],
                 [81,123,240,443,353,508],
                 [57,33,132,268,492,732]]
        
        

        

    def potentialMoves(self,d): #checking board legal moves for die d
        moves = []
        coords = d.getCoord()

        if coords[1] + 1 <= 5 :
            moves.append("r")

        if coords[1] - 1 >=0:
            moves.append("l")

        if coords[0] + 1 <= 5:
            moves.append("f")

        if coords[0] -1 >= 0:
            moves.append("b")

        return moves


    def getBoardValue(self,coords):
        return self.board[coords[0]][coords[1]]



    def tryPotentialMoves(self,d): #seeing if the board legal moves follow the game rules
        
        moveNO = d.getMove()
        potentialMoves = self.potentialMoves(d)
        print (potentialMoves, "potential moves")
        score = d.getScore()

        newDieArr = []

        for move in potentialMoves:
            newDie = copy.deepcopy(d)#creating a new die every potential move, it it's possible we do it
            pStatement =  "Die moving " + move + " from " + str(newDie.getCoord()) + " to "
            newDie.move(move) #faces move around and path updates
           
            

            


            print (pStatement + str(newDie.getCoord()) + " with state: " + str(newDie.getState()))
            print ("Square moved into has value:", self.getBoardValue(newDie.getCoord()))
            
            if newDie.getTop() is not None:
                newScore = score + moveNO * newDie.getTop() 
                print (newScore, "- this would be the new score if die were to move to this square")
                if self.getBoardValue(newDie.getCoord()) == newScore: #if this move was a legeal one, add it to the array
                    newDie.score = newScore
                    newDieArr.append(newDie)

                else:
                    print ("Die tried to move, but move was unsuccessful")


            else:
                print ("Die has None on top side, please fix")
                #TODO
                boardScore = self.getBoardValue(newDie.getCoord())
                findNewFace = (boardScore - score) /moveNO
                print (findNewFace, "THIS IS THE NEW FACE CALCULATED")
                
                newDie.setTop(findNewFace)
                newScore = score + moveNO * newDie.getTop() 
                newDie.score = newScore

                newDieArr.append(newDie)


            newDie.allFaces.append(newDie.faces)
            print (newDie.getState(),"\n")

        return newDieArr

        
        



def startGame():
        
    d = Die()
    g = Game()

    allDice = [d]

    while len (allDice) > 0:
        for i in allDice:
            print ("\n",len(allDice),[i.getCoord() for i in allDice],"\n")
            
            if i.getCoord == [5,5]:
                print ("\n", i.getState())
                return True
            
            childrenDice = g.tryPotentialMoves(i)
            allDice.remove(i) #remove used one

            allDice = allDice + childrenDice #add the successful children dice to the all dice
            


    
startGame()



        

