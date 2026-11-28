'''
Hits on Python OOPs
-------------------
- every thing in python is an object, even classes

            instantiate          initantiate
Metaclass --------------> Class -------------> Object instances

================================================================================
What happens upon calling an Class?
BoilerController()
  1. calls the __call__ method  (Metaclass.__call__() --> BoilerController.__call__())
  2. within __call__, __new__ is invoked, then __init__ is invoked

def __call__(cls, *args, **kwargs):
  # Create object instance
  obj = cls.__new__(cls, *args, **kwargs)

  # Initialize the created instance
  if isinstance(obj, cls):
    obj.__init__(*args, **kwargs)

  return obj
'''
import threading


# Metaclass, that restricts multiple instance creation
# _instance is dict, so that it's used with different classes to prevent multiple instance
class SingletonMetaclass(type):
  _instance = {}
  _lock = threading.Lock()

  def __call__(cls, *args, **kwargs):
    # When using multiple threads to prevent if two threads try to create a object instance
    with cls._lock:
      if cls in cls._instance:
        raise RuntimeError(f"{cls} already Initialized. Use {cls.__name__}.get_instance() instead")

      # Initialize the Object instance (call __new__ followed by __init__)
      cls._instance[cls] = super().__call__(*args, **kwargs)
      return cls._instance[cls]


  def get_instance(cls):
    if cls not in cls._instance:
      raise RuntimeError(f"{cls} is not Initialized")

    return cls._instance[cls]

################################################################################

# Instead of using regular metaclass, using the provided metaclass
# SingletonMetaclass - prevent multiple instances of class being created
class BoilerController(metaclass=SingletonMetaclass):
  def __init__(self, temp_threshold: float):
    self.temp_threshold = temp_threshold
    self._capactiy = 100
    self._size = 0

  def is_fill(self):
    return self._size >= self._capactiy




br = BoilerController(temp_threshold=170)
bz = BoilerController.get_instance()
print(f"br: {br}, bz: {bz}")
