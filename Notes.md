DESIGN PATTERNS (Building Extensible Object-Oriented Software)
==============================================================

##### Inheritance:
* is a OOPs feature, in which the child/subclass automatically retrieves attributes
    and methods from an existing class
* answers 'is-a' relationship
* EX: class A is a parent of class B

##### Composition:
* is a design principle(guideline to follow), in which an class extends it's
    functionality by containing instance of other class rather than inheriting it
* answers 'has-a' relationship
* EX: class A has class B's functionality



SOFTWARE DESIGN PATTERNS
=========================
GOAL: as the code base grows, how to Structure, Extent & Maintain the code

Patterns are categorized into three categories,
1. Creational patterns (how objects are created)
2. Structural patterns (how objects are organized in larger structure)
3. Behavioral patterns (how objects communicate and share responsibility)
    1. Strategy
    2. Observer
 


Strategy Pattern
----------------
- define multiple behaviours, put each in a class => based on need,
   the object uses these behaviours

```python
from abc import ABC, abstractmethod

# Strategy Abstract Class
class Payment(ABC):
  @abstractmethod
  def pay(self, amount:int): ...

# Strategy Implementation Class (behaviours)
class UPIPayment(Payment):
  def pay(self, amount:int):
    print(f"Amount {amount} received by UPI payment")

class CardPayment(Payment):
  def pay(self, amount:int):
    print(f"Amount {amount} received by Card payment")

class CashPayment(Payment):
  def pay(self, amount:int):
    print(f"Amount {amount} received by Cash payment")

# Context
class ShoppingCart:
  def __init__(self, payment_type:Payment):
    self.payment_type = payment_type

  def checkout(self, total:int):
    self.payment_type.pay(total)


# Usage (based on needs, behaviour is replaced)
user1 = ShoppingCart(UPIPayment())
user1.checkout()

user2 = ShoppingCart(CardPayment())
user2.checkout()

# duckA.py: using inheritance, try to mimic this pattern
# duckB.py: using interface, behaviour in individual class
# duckC.py: using interface, behaviour as separate class (added to individual class)
```



Observer Pattern
----------------
- Uses Publisher-Subscriber model
- Publisher/Subject Object: object which is monitored and publishes update
- Observing Object        : objects that are subscribed to publisher objects
- all objects which are subscribed will be notified 
   about any events that happen to the object they are observing

```python
# Observer Interface
class Observer(ABC):
  @abstractmethod
  def sent_notification(self, channel:str, video:str): ...

# Subject/Publisher Interface
class Subject(ABC):
  @abstractmethod
  def register_observer(self, observer:Observer): ...

  @abstractmethod
  def unregister_observer(self, observer:Observer): ...

  @abstractmethod
  def notify_observer(self, video:str): ...

# Subject Class
class YouTubeChannel(Subject):
  def __init__(self, name:str):
    self.name = name
    self._observers = []

  def register_observer(self, observer:Observer):
    self._observers.append(observer)

  def unregister_observer(self, observer:Observer):
    self._observer.remove(observer)

  def notify_observer(self, video:str):
    for observer in self._observers:
      observer.sent_notification(self.name, video)

# Observer Class
class YouTubeUser(Observer):
  def __init__(self, name:str):
    self.name = name

  def sent_notification(self, channel:str, video:str):
    print(f"New Video {video} for channel {channel}")

# -------------------------------------------------------------------
channel = YouTubeChannel('ElectroBoom')

ramu = YouTubeUser('Ramu')
somu = YouTubeUser('Somu')

channel.register_observer(rame)
channel.register_observer(somu)

channel.notify_observer('How to make Tesla Generator?')

# weather_station.py: implements observer pattern
```
