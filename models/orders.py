class Order():
    """Order Model"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, metalId, caretsId, styleId, timeStamp):
        self.id = id
        self.metalId = metalId
        self.caretsId = caretsId
        self.styleId = styleId
        self.timeStamp = timeStamp