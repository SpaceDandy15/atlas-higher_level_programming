#!/usr/bin/python



cl
class Rectangle:
    
  
"""Represent a rectangle."""

    

    de


 
def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the new rectangle.
            height (int): the height of the new rectangle.
        """
        self.width = width
        self.height = height


        self.width = width
        self.height = he

        self.width = width
        self.heig

        self.width = width
 

        self
    @property
    def width(self):
        
 
"""Get/set the width of the rectangle."""
        return self.__width



  
    @width.setter
    
   
def width(self, value):
        
      
if not isinstance(value, int):
            
            r
raise TypeError("width must be an integer")  # Fixed typo here
        
        

   
if value < 0:
            
           

   
raise ValueError("width must be >= 0")
        self.__width = value


        self.__width = value

   

        self.__width = value


        self.__width =
    @property
    
   
def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            
            

 
raise ValueError("height must be >= 0")
        self.__height = value

        self.__height = valu

        self.__height =
