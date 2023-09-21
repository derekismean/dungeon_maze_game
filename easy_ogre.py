import entity
import random

class EasyOgre(entity.Entity):
  def __init__(self, name, max_hp):
    '''
      Represents the hero
      Attributes:
        _name: name of the hero
        _ max_hp: max hp of the hero
    '''
    super().__init__(name, max_hp)

    self._name = "Obtuse Ogre"
    
    rand_hp = random.randint(3, 5)
    self._max_hp = rand_hp
    self._hp = rand_hp

  def attack(self, entity):
    '''
    Enemy attacks the hero and returns a string of the action
    '''
    rand_dmg = random.randint(1, 4)
    entity.take_damage(rand_dmg)
    return self.get_name + " attacks " + entity.get_name + " for " + str(rand_dmg) + " damage.\n"