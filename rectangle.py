
#  Created a class named Rectangle.
class Rectangle:

# Used the __init__()function to assign values to lengh and width

    def __init__(self, length, width):
        self.length=length
        self.width=width

# Inserted a function that returns A=wl
    def area_of_rectangle(self):
        return (self.width*self.length)

# Execute
new_rectangle=Rectangle(8, 6)
print(new_rectangle.area_of_rectangle())


