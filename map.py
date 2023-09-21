class Map:
  '''
  Class Variables:
    _instance: tracks instance of map
    _initialized: tracks if map is initialized
  '''
  _instance = None
  _initialized = False

  def __new__(cls):
    '''
    Constructs map if it hasn't been constructed and stores it in an instance. If it has then it returns the instance.
    '''
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance
  
  def __init__(self):
    '''
    Represents maps
    Attributes:
      _map: map with all the item values
      _revealed: map that shows if the hero has already checked that room
    '''
    if not Map._initialized:
      self.load_map(1)       
    Map._initialized = True
    
  def load_map(self, map_num):
    if map_num == 1:
      file = open("map.txt", "r").read().splitlines()
    elif map_num == 2:
      file = open("map2.txt", "r").read().splitlines()
    elif map_num == 3:
      file = open("map3.txt", "r").read().splitlines()
    
    self._map = []
    for line in file:
      map_1 = []
      for ch in line:
        map_1.append(ch)
      self._map.append(map_1)
      
    self._revealed = []
    for line in file:
      revealed_map = []
      for ch in line:
        revealed_map.append(False)
      self._revealed.append(revealed_map)
    
  def __getitem__(self, row):
    '''
    Overloaded operator that returns the specified row from the map
    '''
    return self._map[row]

  def __len__(self):
    '''
    Overloaded operator that reurns the number of rows in the map list
    '''
    return len(self._map)

  def show_map(self, loc):
    '''
    Returns that map as a string in the format of a 5x5 matrix of characters.
    '''
    map_string = ""
    current_column = 0
    for row in self._map:
      current_row = 0
      for item in row:
        if loc[0] == current_row and loc[1] == current_column:
          map_string += "* "
        else:
          if self._revealed[current_column][current_row] == True or self._map[current_column][current_row] == "s":
            map_string += item
            map_string += " "
          else:
            map_string += "x "
        current_row += 1
      current_column += 1
      map_string += "\n"
    return map_string
      
  def reveal(self, loc):
    '''
    Sets the value in the 2D revealed list at the specified location to True.
    '''
    self._revealed[loc[1]][loc[0]] = True

  def remove_at_loc(self, loc):
    '''
    Overwrites the character in the map list at the specified location with an 'n'.
    '''
    self._map[loc[1]][loc[0]] = "n"

