from enum import Enum
from ObjectOperations import Operations

class Weights(Enum):
    sameIncr = .1 # same general property increment value
    angleIncr = 20   # same angle rotation transform increment value
    reflectIncr = 15  # same reflection transform increment value
    fillIncr = 40  # increment for correct fill transformation
    shapeIncr = 100 # increment for correct shape transformation
    deleteIncr = 200 # increment for correct deletion of objects
    deleteCompIncr = 4 # increment for compensation for deleted/added objects having less matches
    alignIncr = 35 # increment for correct alignment transformation
    sizeIncr = 50 # increment for correct size transformation
    overlapsIncr = 21 # increment for correct overlap transformation
    overlapsBoolIncr = 10 # increment for correct overlap boolean transformation
    leftOfIncr = 20 # increment for correct left-of transformation
    aboveIncr = 20 # increment for correct above transformation

class ProblemSolver:
        

    def __init__(self, problem):
        self.problem = problem
        self.oo = Operations() 
        self.p1 = problem.figures['1']
        self.p2 = problem.figures['2']
        self.p3 = problem.figures['3']
        self.p4 = problem.figures['4']
        self.p5 = problem.figures['5']
        self.p6 = problem.figures['6']
        self.a = problem.figures['A']
        self.b = problem.figures['B']
        self.c = problem.figures['C']
        self.answer = -1 
        self.maxTot = 0   # initiate a best answer score variable to 0
        self.matchObjsDict = {}





        #compare objecst for size and matching properties
    def FillObjectDictionary(self):
        matchObjsDict = self.oo.matchObjects(self.a, self.b, self.matchObjsDict)
        matchObjsDict = self.oo.matchObjects(self.a, self.c, self.matchObjsDict)
       
        for x in range(1,7):
            ans = self.problem.figures[str(x)]
            matchObjsDict = self.oo.matchObjects(self.b,ans,self.matchObjsDict)
            matchObjsDict = self.oo.matchObjects(self.c,ans,self.matchObjsDict)



    def GetAnswer(self):
        self.FillObjectDictionary()
        return self.answer 