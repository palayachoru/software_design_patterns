DESIGN PATTERNS (Building Extensible Object-Oriented Software)
--------------------------------------------------------------

STRATEGY PATTERN
================

Using Inheritance:
------------------
```
Duck Class
 |- Mallard Duck
 |- Redhead Duck
 |- Rubber Duck
 |- Wooden Duck

(refer duckA.py)
```
 Problems with this approach
 * if base class has a method, then if the subclass need it or not -- it will be inherited
 * in case if subclass don't needs a method, then need to manually override it
 * maintaining a large number of manual override is error prone


Using Interface + logic in individual class
--------------------------------------------
```
Interface:
Fly
Sound

Base Class:
Duck

MallardDuck(Duck, Fly)
RubberDuck(Duck, Sound)

(refer duckB.py)
```
- interface don't provide behaviour to class that inherits it
- individual class has to define it's behaviour
- idea of interface is to make promise that the inherited class has that method

Problems with this approach
* if two subclass has similar Fly behaviour, then code repetition happens
* No code reusability with this approach
* if need to modify a behaviour, then need to track down all subclass that
  has that behaviour and modify it - which is error prone



Using Interface + logic in separate class (as behaviour)
--------------------------------------------------------
```
Interface:
FlyBehaviour
Sound

Behaviour Implementation:
FlywithWings(FlyBehaviour)
NoFly(FlyBehaviour)
QuackSound(Sound)

Base Class:
Duck(flybehaviour, sound)


MallardDuck(Duck)
  init(FlywithWing(), QuackSound())

(refer duckC.py)
```
- the behaviour is taken out of the class and added to class based on needed
- in case a class don't need it, just remove it
- and if we need to modify a behaviour, it's easy to vary and all class that
   uses the behaviour get updated
- easy to maintain and update the code based on varying requirement
- this way of using other classes with in another class is called 'Composition'

- using this approach, we can dynamically alter or add new behaviour to a class
- that's why this approach/pattern is called "Strategy Pattern"

###### Strategy Pattern
- defines a family of algorithm(behaviour) that can be interchangeable
- so define a task separately from where it's used and the object use these tasks
   based on requirement without defining in each object


HINT:
* always try to use Composition over Inheritance


---


OBSERVER PATTERN
================
- works similar to Publisher-Subscriber model
- if the objects are subscribed to a publisher(subject) and if it changes
   a notification is sent to all the subscribers(observers)
- defined as One-to-Many relationship b/w set of objects, so when the state of
   the object changes all the dependent objects are notified/updated

Loose coupling:
- two objects can interact but know less about each other
ie.
  - modifying one don't impact other object
  - 

HINT:
* always try to go for loosely coupled designs b/w objects that interact


---


DECORATING PATTERN
===================
