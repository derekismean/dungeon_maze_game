import enemy_factory
import random
import easy_troll
import easy_ogre
import easy_goblin

class BeginnerFactory(enemy_factory.EnemyFactory):
  ''' Factory to create easy enemies.'''
  def create_random_enemy(self):
    ''' Randomizes and constructs one of the easy enemies'''
    random_num = random.randint(1,3)
    if random_num == 1:
      ''' Construct EasyTroll object'''
      return easy_troll.EasyTroll("",0)
    elif random_num == 2:
      ''' Construct EasyOgre object'''
      return easy_ogre.EasyOgre("",0)
    else:
      ''' Construct EasyGoblin object'''
      return easy_goblin.EasyGoblin("",0)