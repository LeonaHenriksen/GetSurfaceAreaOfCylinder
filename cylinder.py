from math import pi

class Cylinder:
  def __init__(self, height=None, radius=None):
    self.height = height
    self.radius = radius
  
  def get_surface_area(self):
    if self.height == None:
      self.height = float(input("Enter the height of the cylinder: "))
                  
    if self.radius == None:
      self.radius = float(input("Enter the radius of the cylinder: "))
  
    area = 2 * pi * self.radius * (self.radius + self.height)
    
    print("The area of the cylinder is {:.2f}".format(area))
                