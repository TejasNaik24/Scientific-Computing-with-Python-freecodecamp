class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        """Set the width of the rectangle"""
        self.width = width
    
    def set_height(self, height):
        """Set the height of the rectangle"""
        self.height = height
    
    def get_area(self):
        """Return the area of the rectangle"""
        return self.width * self.height
    
    def get_perimeter(self):
        """Return the perimeter of the rectangle"""
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        """Return the diagonal of the rectangle"""
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        """Return a string representation of the rectangle using asterisks"""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self, shape):
        """Return how many times the passed shape can fit inside this shape"""
        width_fits = self.width // shape.width
        height_fits = self.height // shape.height
        return width_fits * height_fits
    
    def __str__(self):
        """String representation of the rectangle"""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        """Initialize a square with equal width and height"""
        super().__init__(side, side)
    
    def set_side(self, side):
        """Set both width and height to the same value"""
        self.width = side
        self.height = side
    
    def set_width(self, width):
        """Set both width and height when setting width"""
        self.set_side(width)
    
    def set_height(self, height):
        """Set both width and height when setting height"""
        self.set_side(height)
    
    def __str__(self):
        """String representation of the square"""
        return f"Square(side={self.width})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())
    
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
    
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))