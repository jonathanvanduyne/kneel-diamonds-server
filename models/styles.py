class Style():
    """Style Model for storing style related details"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, style, price):
        self.id = id
        self.style = style
        self.price = price