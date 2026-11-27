from abc import ABC, abstractmethod

'''
Coffee        Cost
---------------------
House blend   10
Dark rost     25
Decaf         10
Espresso      30

Condiment   Cost
--------------------
Mocha         5
Whip          11
Milk          40
Soy           10

There are 4 types of coffee and for each of those, we can add multiple condiments
and the price will be increased according to the no of condiments added

Coffee -> Main Class
Condiment -> Decorator class

Both the main & decorator class must have same parent, so that main & decorator
class can we wrapped on top of one another.
'''

# Main Interface
class Coffee(ABC):
  @abstractmethod
  def beverage(self)->str:...

  @abstractmethod
  def cost(self)->int: ...


# Decorator Interface (Abstract + Protected reference(self._base))
# uses @abstractmethod, to prevent direct initialization of objects
class CoffeeCondiment(Coffee, ABC):
  def __init__(self, coffee:Coffee):
    self._base = coffee

  @abstractmethod
  def beverage(self) -> str:
    return self._base.beverage()

  @abstractmethod
  def cost(self)->int:
    return self._base.cost()


################################################################################
# Main implementation (types of Coffee)
class HouseBlend(Coffee):
  def beverage(self) -> str:
    return 'House Blend'

  def cost(self) -> int:
    return 15


class Espresso(Coffee):
  def beverage(self) -> str:
    return 'Espresso'

  def cost(self) -> int:
    return 30


class DarkRost(Coffee):
  def beverage(self) -> str:
    return 'Dark Rost'

  def cost(self) -> int:
    return 25


################################################################################
# Contiments implementation
class MochaCondiment(CoffeeCondiment):
  def beverage(self) -> str:
    return super().beverage() + ' /w Mocha'

  def cost(self) -> int:
    return super().cost() + 5


class WhipCondiment(CoffeeCondiment):
  def beverage(self) -> str:
    return super().beverage() + ' /w Whip'

  def cost(self) -> int:
    return super().cost() + 11



################################################################################
# Usage
hb = HouseBlend()
hb_whip = WhipCondiment(hb)
hb_mocha_whip = MochaCondiment(hb_whip)

print(f"{hb_whip.beverage()}: INR {hb_whip.cost()}")
print(f"{hb_mocha_whip.beverage()}: INR {hb_mocha_whip.cost()}")
