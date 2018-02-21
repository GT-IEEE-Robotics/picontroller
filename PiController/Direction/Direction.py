import numpy as np

class Coordinate(np.ndarray):
  def __new__(cls, x,                  # Required argument - x coordinate
                   y,                  # Required argument - y coordinate
                   theta,              # Required argument - inclination of the robot with respect to the x axis.
                   info = None):              # Optional argument - Info about the numpy array in case you want to tag it with some information.
  
  
    # Sanitizing x and y values
    if (
        x is None or
        y is None or
        theta is None
       ):
      raise ValueError('Incomplete coordinate input. Please enter valid x, y & theta')
    
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    if (
        not (is_number(x) and
             is_number(y) and
             is_number(theta)
            )
       ):
      raise ValueError('Incorrect input. Please use numbers only for x, y & theta arguments')
    # We need to make ndarray instance using x, y & theta values.
    dimension = np.dtype({'names':  ('x',  'y',  'theta'),
                          'formats':('f8', 'f8', 'f8')})
    input_array = np.array([(x,y,theta)],dimension)
    # We first cast to be our class type
    obj = np.asarray(input_array).view(cls)
    # add the new attribute to the created instance
    obj.info = info
  
    # Finally, we must return the newly created object:
    return obj
  def __array_finalize__(self, obj):
    # see InfoArray.__array_finalize__ for comments
    if obj is None: return
    self.info = getattr(obj, 'info', None)
  def __add__(self,other):
  
    return Coordinate(self["x"][0]     + other["x"][0],
                      self["y"][0]     + other["y"][0],
                      self["theta"][0] + other["theta"][0])
  def __sub__(self,other):
  
    return Coordinate(self["x"][0]     - other["x"][0],
                      self["y"][0]     - other["y"][0],
                      self["theta"][0] - other["theta"][0])

if __name__=="__main__":
  start = Coordinate(1,2,0)
  finish = Coordinate(4,5,0)
   
  print("The distance between start and finish is")
  distance = finish - start
  print(distance)

class Compass(object):
  N, NE, E, SE, S, SW, W, NW = range(1,9)
  CW, CCW = range(9,11)

  def __init__(self,value):
    if isinstance(value,basestring):
      self.value = Compass.convert(value)
      #If the user enters in a string instead of a number or the class defined static variables, convert it to the string.
    elif 1 <= value <= 10:
      self.value = value
    else:
      raise ValueError("Compass is given invalid argument")
  def __repr__(self):
    return "Compass Direction" + Compass.convert(self.value)  #Should return the string representation of the value
  @staticmethod
  def convert(direction = None):
    #Sanitizing inputs
    if direction == None:
        raise ValueError('Compass direction is not given. Please enter valid input')
  
    # If the input is a number, return a string
    if 1 <= direction <= 10:
       directionList = {
        1:"N",
        2:"NE",
        3:"E",
        4:"SE",
        5:"S",
        6:"SW",
        7:"W",
        8:"NW",
        9:"CW",
        10:"CCW"
       }
       direction_raw = directionList.get(direction, None)
       if direction_raw is not None:
         return direction_raw
       else:
         raise ValueError('Compass direction should be a valid integer number from 1 to 10')
    # If the input is a string, return a number
  
    if isinstance(direction, basestring):
      directionList = {
          # Actual Directions
          "N"   : Compass.N,
          "NE"  : Compass.NE,
          "E"   : Compass.E,
          "SE"  : Compass.SE,
          "S"   : Compass.S,
          "SW"  : Compass.SW,
          "W"   : Compass.W,
          "NW"  : Compass.NW,
          # Spins the robot
          "CW"  : Compass.CW,
          "CCW" : Compass.CCW
       }
      direction_raw = directionList.get(direction, None)
      if 1 <= direction_raw <= 10:
        return direction_raw
      else:
        raise ValueError('Compass direction should be a valid string as an input.')
       # Somehow, you've reached here. This should not happen but whatever, raise the error
      raise ValueError('Invalid input - input entered is neither string nor number')

# Defining keywords for people to use
# When this package is imported, the user should be able to use the keywords without worrying about refering to the correct class name.
# In short, they can use N, NW and so on without saying CompassDirection.N or anything like that.

N   = Compass.N
NE  = Compass.NE
E   = Compass.E
SE  = Compass.SE
S   = Compass.S
SW  = Compass.SW
W   = Compass.W
NW  = Compass.NW
CW  = Compass.CW
CCW = Compass.CCW
