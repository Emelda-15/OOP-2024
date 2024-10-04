class MathOperations:
    multiplier = 5  # class variable

    @classmethod
    def set_multiplier(cls, value):
        cls.multiplier = value  # modify class variable

    @staticmethod
    def add(a, b):
        return a + b

    def multiply(self, a):
        return a * self.multiplier  # instance method

# Using class method
MathOperations.set_multiplier(10)

# Using static method
print(MathOperations.add(3, 4))  # Output: 7

# Using instance method
obj = MathOperations()
print(obj.multiply(6))  # Output: 60
