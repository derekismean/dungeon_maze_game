import abc

class EnemyFactory(abc.ABC):
  ''' Enemy factory interface '''
  @abc.abstractmethod
  def create_random_enemy(self):
    pass