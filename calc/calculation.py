""" This is our base class : Calculation """
# This is an abstract class
# This is where we create our objects
class Calculation:
    """ This is the Calculation class """

    def __init__(self, value_a, value_b):
        """ This is the Calculation constructor """
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method
    @classmethod
    def instantiate(cls, value_a, value_b):
        """ This instantiates an object """
        return  cls(value_a, value_b)

    # This satisfies the "Too few public methods" pylint error
    def set(self, value_a, value_b):
        """ Set the value_a and value_b values """
        self.value_a = value_a
        self.value_b = value_b
