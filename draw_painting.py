class Draw_painting:
    def __init__(self, sam):
        self.sam = sam

    def turn_left(self):
        """Turns left for the next line"""
        self.sam.left(90)
        self.sam.forward(30)
        self.sam.left(90)
        self.sam.forward(30)

    def turn_right(self):
        """Turns right for ther next line"""
        self.sam.right(90)
        self.sam.forward(30)
        self.sam.right(90)
        self.sam.forward(30)

    def draw_dot(self, color):
        """Draws the dot"""
        self.sam.dot(20, color)
        self.sam.penup()
        self.sam.forward(30)
        self.sam.pendown()