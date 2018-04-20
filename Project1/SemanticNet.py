class SemanticNet:
    shape = ""
    fill = ""
    size = ""
    name = ""


    def __init__(self):
        pass

    def SetShape(self, shape):
        self.shape = shape

    def SetFill(self, fill):
        self.fill = fill

    def SetName(self, name):
        self.name = name

    def SetSize(self, size):
        self.size = size

    def HasShapeDeleted(self, count1, count2):
        if count1 != count2:
            return True
        else:
            return False


    def BuildAB(self, figureA, figureB):
        pass