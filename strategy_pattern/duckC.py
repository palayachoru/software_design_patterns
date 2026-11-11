from abc import ABC, abstractmethod

# Interface for behaviours
class FlyBehaviour(ABC):
  @abstractmethod
  def fly(self) -> str: ...

class SoundBehaviour(ABC):
  @abstractmethod
  def sound(self) -> str: ...


# Implementation of each behaviour types
class FlywithWings(FlyBehaviour):
  def fly(self) -> str:
    return "Fly fly"

class NoWings(FlyBehaviour):
  def fly(self) -> str:
    return "<< No FLy >>"

class FlywithJetPacks(FlyBehaviour):
  def fly(self) -> str:
    return "Peeeee!!!"


class QuackSound(SoundBehaviour):
  def sound(self) -> str:
    return "Quack Quack"

class MuteSound(SoundBehaviour):
  def sound(self) -> str:
    return "<< Silence >>"



# Base Class
class Duck:
  def __init__(self, flybehaviour, soundbehaviour):
    self.fly_behaviour = flybehaviour
    self.sound_behaviour = soundbehaviour

  def fly(self) -> str:
    ''' Delegating the task to the behaviour class '''
    return self.fly_behaviour.fly()

  def sound(self) -> str:
    return self.sound_behaviour.sound()


# Each behaviour of duck it attached via behaviour class

class MallardDuck(Duck):
  def __init__(self):
    super().__init__(FlywithWings(), QuackSound())


# Here we dynamically altering the behaviour of the duck
# When attach_jetpack() is called, the WoodenDuck got fly behaviour
class WoodenDuck(Duck):
  def __init__(self):
    super().__init__(NoWings(), MuteSound())

  def attach_jetpack(self):
    self.fly_behaviour = FlywithJetPacks()


# So advantage of this approach
# 1. behaviour can be modified in run time based on needs
# 2. maintaining behaviour is also easy as it's not inner in a class
