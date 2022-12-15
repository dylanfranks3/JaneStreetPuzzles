class Die:
    def __init__(self,state,faces = None): 
        if not faces:
            self.faces = [0.5,0.5,0.5,0.5,0.5,0.5] #default values
        else:
            self.faces = faces
        self.state = state #[UP, FRONT] INDEX OF WHAT FACES  
        #default state is one is up, two is front

        #faces take the form, [up,front,left,right,back,bottom] 

    def move(self,direction): #direction can take form f,b,l,r -> will return the state
        if direction == "f":
            self.state = [self.state[1],5-self.state[0]]

        if direction == "b":
            self.state = [5-self.state[1],self.state[0]]

        if direction == "l":
            self.state = [,self.state[1]]

        if direction == "r":
            self.state = [,self.state[1]]
        return self.state
            



        

