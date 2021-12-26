class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print(f'Called constructor: {x}, {y}')

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")
    
point = Point(10,20)
point.move()
point.draw()
point.x=100
print(point.x)