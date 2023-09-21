import entity
import map
import random

class Hero(entity.Entity):
  def __init__(self, name, max_hp):
    '''
      Represents the hero
      Attributes:
        _name: name of the hero
        _ max_hp: max hp of the hero
    '''
    super().__init__(name, max_hp)
    self._loc = [0, 0]

  # Returns location of the hero
  @property
  def get_loc(self):
    return self._loc

  def attack(self, entity):
    '''
    Hero attacks the enemy and returns a string of the action
    '''
    rand_dmg = random.randrange(2,6)
    entity.take_damage(rand_dmg)
    return self.get_name + " attacks " + entity.get_name + " for "+ str(rand_dmg) + " damage."

  def go_north(self):
    '''
    Makes the hero move north and returns an "x" if the hero try to move out of bound
    '''
    if self._loc[1] <= 0:
      return "x"
    else:
      self._loc[1] -= 1
      return self.get_loc
      
  def go_south(self): 
    '''
    Makes the hero move north and returns an "x" if the hero try to move out of bound
    '''
    m = map.Map()
    if self._loc[1] >= len(m) - 1:
      return "x"
    else:
      self._loc[1] += 1
      return self.get_loc

  def go_east(self):
    '''
    Makes the hero move north and returns an "x" if the hero try to move out of bound
    '''
    m = map.Map()
    if self._loc[0] >= len(m) - 1:
      return "x"
    else:
      self._loc[0] += 1
      return self.get_loc
    
  def go_west(self):
    '''
    Makes the hero move north and returns an "x" if the hero try to move out of bound
    '''
    if self._loc[0] <= 0:
      return "x"
    else:
      self._loc[0] -= 1
      return self.get_loc


