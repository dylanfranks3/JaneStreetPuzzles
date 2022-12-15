class Die:
    def __init__(self): 
        self.faces = [None,None,None,None,None,None] #init as None before faces are known
        self.score = 0
        self.coord = [0,0]
        self.path = [] #append path through board
        #default faces is one is up, two is front

        #faces take the form, [top,front,left,right,back,bottom] 

    def move(self,direction): #direction can take form f,b,l,r -> will return the faces
        if direction == "f":
            self.faces = [self.faces[1],
                        self.faces[5],
                        self.faces[2],
                        self.faces[3],
                        self.faces[0],
                        self.faces[4]]

        if direction == "b":
            for i in range(3): #backwards is forwards 3x
                self.move("f")

        if direction == "l":
            self.faces = [self.faces[3],
                        self.faces[1],
                        self.faces[0],
                        self.faces[5],
                        self.faces[4],
                        self.faces[2]]

        if direction == "r":
            for i in range(3): #right is left 3x
                self.move("l")
            
        
        return self.faces
    
    def getTop(self): 
        return self.faces[0]
    
    def getMove(self):
        return len(self.path) + 1

    

            

class Game:
    def __init__(self):
        self.board = [[0,77,32,403,337,452],
                 [5,23,-4,592,445,620],
                 [-7,2,357,452,317,395],
                 [186,42,195,704,452,228],
                 [81,123,240,443,353,508],
                 [57,33,132,268,492,732]]
        
        self.die = []

        

    def potentialMoves(self,coord): #checking board legal moves
        moves = []
        if coord[0] + 1 < 6 :
            moves.append("f")

        if coord[0] - 1 >0:
            moves.append("b")

        if coord[1] + 1 < 6:
            moves.append("r")

        if coord[1] -1 > 0:
            moves.append("l")

        return moves



    def tryPotentialMoves(self):
        pass

    

        
    
        



        

