import enemy_factory
import random
import troll
import ogre
import goblin

class ExpertFactory(enemy_factory.EnemyFactory):
  ''' Factory to create easy enemies.'''
  def create_random_enemy(self):
    ''' Randomizes and constructs one of the easy enemies'''
    random_num = random.randint(1, 4)
    if random_num == 1:
      ''' Construct Troll object'''
      return troll.Troll("",0)
    elif random_num == 2:
      ''' Construct Ogre object'''
      return ogre.Ogre("",0)
    else:
      ''' Construct Goblin object'''
      return goblin.Goblin("",0)