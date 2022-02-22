class Rectangle:
    def __init__(self, width, height):
        assert width > 0, 'width should be greater than zero'
        assert height > 0, 'height should be greater than zero'
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self): 
        return 2 * self.width + 2 * self.height
    def get_diagonal(self): 
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic =''
        for i in range (self.height):
            for j in range (self.width):
                pic += '*'
            pic += '\n'

        return pic
    def get_amount_inside(self, sq):        
        x = self.width / sq.width
        y = self.height / sq.height

        if x >= 1 and y > 1:
            result = int(x * y)        
            return result        
        return 0
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
class Square(Rectangle):
    def __init__(self, side):
        assert side > 0, 'side should be greater than zero'
        super().__init__(side, side)
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
    def __str__(self):
        return f"Square(side={self.height})"
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.height = height
        self.width = height
