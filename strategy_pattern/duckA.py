class Duck:
  def fly(self) -> str:
    return "Fly fly"

  def sound(self) -> str:
    return "Quack Quack"



# MallardDuck just inherits all behaviour and that's is
class MallardDuck(Duck):
  pass



# RedheadDuck has to override only one behaviour
class RedheadDuck(Duck):
  def fly(self) -> str:
    return "I can't fly high"



# RubberDuck has to override both the methods from parent class
class RubberDuck(Duck):
  def fly(self) -> str:
    return "I don't have wings"

  def sound(self) -> str:
    return "Squeak Squeak"


# RubberDuck has to override both the methods from parent class
class WoodenDuck(Duck):
  def fly(self) -> str:
    return "I don't have wings"

  def sound(self) -> str:
    return "<< silence >>"
