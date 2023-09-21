import abc

class Entity(abc.ABC):
  def __init__(self, name, max_hp):
    '''
    Represents an entity
    Attributes:
      _name: name of the entity
      _max_hp: max hp of the entity
      _hp: current hp of the entity
    '''
    self._name = name
    self._max_hp = max_hp
    self._hp = self._max_hp

  # Returns name of the entity
  @property
  def get_name(self):
    return self._name

  # Returns current hp of the entity
  @property
  def get_hp(self):
    return self._hp

  def take_damage(self, dmg):
    '''
    The entity's health decreases by amount of damage received, resets to 0 if health is negative 
    '''
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0

  def heal(self):
    self._hp = self._max_hp
      
  def __str__(self):
    '''
    Returns string that displays the entity's name and health
    '''
    return self.get_name + "\n" + "HP: " + str(self.get_hp) + "/" + str(self._max_hp)

  # abstract method of entity attack
  @abc.abstractmethod
  def attack(self, entity):
    pass