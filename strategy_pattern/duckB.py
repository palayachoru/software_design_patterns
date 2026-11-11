from abc import ABC, abstractmethod

# Abstract class, that gives promise that all the subclass has method implementation
class Flyable(ABC):
  @abstractmethod
  def fly(self) -> str:
    ...                # means there is not implementation


class Sound(ABC):
  @abstractmethod
  def sound(self) -> str:
    ...


# Base Class
class Duck:
  pass


# Even though, MallardDuck & RedheadDuck has same sound behaviour
# the code repetition happens, no code reusability with this approach
class MallardDuck(Duck, Flyable, Sound):
  def fly(self) -> str:
    return "Fly fly"

  def sound(self) -> str:
    return "Quack Quack"


class RedheadDuck(Duck, Flyable, Sound):
  def fly(self) -> str:
    return "I don't have wings"

  def sound(self) -> str:
    return "Quack Quack"


class WoodenDuck(Duck, Flyable, Sound):
  def fly(self) -> str:
    return "I don't have wings"

  def sound(self) -> str:
    return "<< silence >>"
