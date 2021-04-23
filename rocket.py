
# A simulator for a rocket ship in a game.
class Rocket:

# The __init__() method doesn't take any arguments but sets the x and y positions to zero.
    def __init__(self):
        self.x=0
        self.y=0

# Move_up() - will increment y position by 1
    def move_up(self):
        self.y+=1

# Move_right() - will increment x position by 1
    def move_right(self):
        self.x+=1


# Move_down() - will decrement y position by 1
    def move_down(self):
        self.y-=1

# Move_left() - will decrement x position by 1
    def move_left(self):
        self.x-=1

# Current_postition() - will print the  current position of the Rocket]
    def current_postition(self):
        return self.y, self.x

current_postition=Rocket()
print(current_postition)