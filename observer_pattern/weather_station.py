from __future__ import annotations

import random
from time import sleep
from abc import ABC, abstractmethod


'''
Interface of Observer and Suject defines the required method for this pattern

Subject is loosly tied with Observer object, such that when ever the values
changes, it calls the update() method of observer. That's it.

So the Observer instance has to be created and it has to added as observer
to the Subject object.

Using this approach, new observers can we added or removed without any
modification to the Suject class
'''

class Observer(ABC):
  @abstractmethod
  def update(self) -> None: ...    # from Subject class, this method is called to notify update


class Subject(ABC):
  @abstractmethod
  def register_observer(self, observer:Observer) -> None: ...

  @abstractmethod
  def remove_observer(self, observer:Observer) -> None: ...

  @abstractmethod
  def notify_observers(self) -> None: ...


################################################################################


class CurrentDisplay(Observer):
  def __init__(self):
    self.temperature = 0
    self.pressure = 0
    self.humidity = 0
    self.subject = None

  def register(self, subject:WeatherData):
    ''' When registering to Subject(Publisher), the instance is also recorded, so
    that it's used while removing the subscription.
    '''
    self.subject = subject
    self.subject.register_observer(self)

  def remove(self):
    if not self.subject: return
    self.subject.remove_observer(self)

  def display(self):
    print(f'CURRENT| TEMP:{self.temperature}, PRES:{self.pressure}, HUMI: {self.humidity}')

  def update(self):
    if not self.subject: return

    self.temperature = self.subject.temperature
    self.pressure = self.subject.pressure
    self.humidity = self.subject.humidity

    self.display()


class ForecastDisplay(Observer):
  def __init__(self):
    self.temperature = 0
    self.pressure = 0
    self.humidity = 0
    self.subject = None

  def register(self, subject:WeatherData):
    ''' When registering to Subject(Publisher), the instance is also recorded, so
    that it's used while removing the subscription.
    '''
    self.subject = subject
    self.subject.register_observer(self)

  def remove(self):
    if not self.subject: return
    self.subject.remove_observer(self)

  def display(self):
    print(f'FORECAST| TEMP:{self.temperature}, PRES:{self.pressure}, HUMI: {self.humidity}')

  def update(self):
    if not self.subject: return

    self.temperature = self.subject.temperature + 10
    self.pressure = self.subject.pressure + 20
    self.humidity = self.subject.humidity + 5

    self.display()



class WeatherData(Subject):
  def __init__(self):
    self._observers = []

  def register_observer(self, observer:Observer):
    ''' Register new observers to get update'''
    self._observers.append(observer)

  def remove_observer(self, observer:Observer):
    ''' Remove the observer'''
    self._observers.remove(observer)

  def notify_observers(self):
    ''' Go through all subscribed observer and call it's update method'''
    for observer in self._observers:
      observer.update()

  @property
  def temperature(self) -> int:
    return random.randint(-10, 40)   # °C

  @property
  def humidity(self) -> int:
    return random.randint(0, 100)  # %

  @property
  def pressure(self) -> int:
    return random.randint(950, 1050)  # hPa

  def measurements_changed(self):
    self.notify_observers()


################################################################################

if __name__ == "__main__":
  # creating a Subject(Publisher) instance
  weather = WeatherData()

  # creating a observer to display current weather
  current_screen = CurrentDisplay()
  current_screen.register(weather)   # register to a subject(publisher)

  # creating a observer to display forecast weather
  forecast_screen = ForecastDisplay()
  forecast_screen.register(weather)

  # simulating weather change
  weather.measurements_changed()
  sleep(3)
  weather.measurements_changed()
  sleep(3)
  weather.measurements_changed()
  sleep(3)
  weather.measurements_changed()
  sleep(3)
  weather.measurements_changed()

  # when ever a change is identified, all the observers are notified
  # as we see the new weather data is updated
