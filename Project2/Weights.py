from enum import Enum

class Weights(Enum):
    counter = .1
    deleteWeight = 200  # increment for correct deletion of objects
    shapeWeight = 100  # increment for correct shape transformation
    sizeWeight = 50  # increment for correct size transformation
    fillWeight = 40  # increment for correct fill transformation
    alignWeight = 35  # increment for correct alignment transformation

    overlapsWeight = 21  # increment for correct overlap transformation
    leftOfWeight = 20  # increment for correct left-of transformation
    aboveWeight = 20  # increment for correct above transformation
    rightOfWeight = 20  # increment for correct above transformation
    angleWeight = 20  # same angle rotation transform increment value
    reflectionWeight = 15  # same reflection transform increment value
    overlapsWeightCtr = 10  # increment for correct overlap boolean transformation
    deleteWeightCtr = 4  # increment for compensation for deleted/added objects having less matches

