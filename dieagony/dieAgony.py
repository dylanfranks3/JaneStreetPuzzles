class Die:
    def __init__(self): 
        
        self.faces = [None,None,None,None,None,None] 
        self.score = 0
        self.coord = [0,0]
        self.path = []
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
            for i in range(3):
                self.move("f")

        if direction == "l":
            self.faces = [self.faces[3],
                        self.faces[1],
                        self.faces[0],
                        self.faces[5],
                        self.faces[4],
                        self.faces[2]]

        if direction == "r":
            for i in range(3):
                self.move("l")
            
        
        return self.faces
    

            



        

