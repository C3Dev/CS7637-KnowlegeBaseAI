#Corey Crooks
#Class for Semantic Network properites/comparisons 
#02/16

import random
from Weights import Weights
class SemanticNet:
    problem = None
    sizeList = {'very small':1, 'small':2, 'medium':3, 'large':4, 'very large':5, 'huge':6}
    def __init__(self):
        pass


    def SetProblem(self, problem):
        self.problem = problem


    def CompareAttributes(self, objectA, objectB, i, transformation, attribute, name):
        attributeName = name.title()
        if name == 'width' or name == 'height' or name == 'size':
            if name in objectA.attributes and name in objectB.attributes:
                objectASize1 = self.sizeList.get(objectA.attributes[name])
                objectBSize1 = self.sizeList.get(objectB.attributes[name])
                transformation[str(i) + attribute + attributeName + 'difference'] = objectASize1 - objectBSize1
        else:
            if name in objectA.attributes and name in objectB.attributes:
                transformation[str(i) + attribute + attributeName + 'difference'] = (objectA.attributes[name]) + (objectB.attributes[name])


    def CalculateTransformScore(self, i, score, transformations, objectNameList, objectNameList1, attribute, weight):
        attributeName = attribute.title()
        fName = str(i)
        if fName + objectNameList + attributeName + 'difference' in transformations and fName + objectNameList1 + attributeName + 'difference' in transformations:
             if (transformations[fName + objectNameList + attributeName + 'difference']) == (transformations[fName + objectNameList1 + attributeName + 'difference']):
                score += weight
        return score



    def CompareObjects(self, objectA, objectB, n, transformations, figName):

        if 'width' in objectA.attributes and 'width' in objectB.attributes:
            widthValue = self.sizeList.get(objectB.attributes['width'])
            transformations[str(n) + figName + 'Widthdifference'] = self.sizeList.get(objectA.attributes['width']) - widthValue

        if 'height' in objectA.attributes and 'height' in objectB.attributes:
            heightValue = self.sizeList.get(objectB.attributes['height'])
            transformations[str(n) + figName + 'Heightdifference'] = self.sizeList.get(objectA.attributes['height']) - heightValue
        return transformations


    def ConvertShape(self, ObjectA, ObjectB):
        if ObjectA.attributes['shape'] == 'square' and 'height' not in ObjectA.attributes and 'width' not in ObjectA.attributes:
            ObjectA.attributes['height'] = ObjectA.attributes['size']
            ObjectA.attributes['width'] = ObjectA.attributes['size']

        if ObjectB.attributes['shape'] == 'square' and 'height' not in ObjectB.attributes and 'width' not in ObjectB.attributes:
            ObjectB.attributes['height'] = ObjectB.attributes['size']
            ObjectB.attributes['width'] = ObjectB.attributes['size']




    def FindDeletedObjects(self, figureA, figureB, c, score, items, objectBItems, problem, counter,transformations, i):

        if figureA is None:
            length1 = 0
        else:
            length1 = len(figureA.objects)
        if figureB is None:
            length2 = 0
        else:
            length2 = len(figureB.objects)
        if c is None:
            length3 = 0
        else:
            length3 = len(c.objects)
        if score is None:
            lengthscore = 0
        else:
            lengthscore = len(problem.figures[str(i)].objects)

        totalLength = length1 - length2 
        lengthtotal = length3 - lengthscore
        transformations[items + 'DifferenceDeleted'] = totalLength
        transformations[objectBItems + 'DifferenceDeleted'] = lengthtotal

        if transformations[items + 'DifferenceDeleted'] == transformations[objectBItems + 'DifferenceDeleted'] and transformations[items + 'DifferenceDeleted'] != 0:
            counter += (Weights.deleteWeight.value * abs(transformations[items + 'DifferenceDeleted']))


        elif transformations[items + 'DifferenceDeleted'] == transformations[objectBItems + 'DifferenceDeleted'] and transformations[
            items + 'DifferenceDeleted'] == 0:
            counter += Weights.deleteWeight.value

        else:  
            if length1 != 0 and length2 != 0 and length3 != 0 and lengthscore != 0:
                transformations[items + 'DeleteMultipleDifferences'] = float(length2) / length1
                transformations[objectBItems + 'DeleteMultipleDifferences'] = float(lengthscore) / length3
                if transformations[items + 'DeleteMultipleDifferences'] == transformations[objectBItems + 'DeleteMultipleDifferences']:
                    counter += Weights.deleteWeight.value * 2
        if lengthscore < min(length1, length2, length3):
            counter += (min(length1, length2, length3) - lengthscore) * Weights.deleteWeightCtr.value

        elif lengthscore > max(length1, length2, length3):
            counter += (lengthscore - max(length1, length2, length3)) * Weights.deleteWeightCtr.value

        return counter


    def EliminDuplicates(self, inputString):
        elimList = ''
        elimList = inputString.split('-')
        item = ''
        deletedWords = []
        for word in elimList:
            if word in item:
                deletedWords.append(word)
            else:
                item += word
        for deletedWord in deletedWords:
            item = item.replace(deletedWord, "")
        return item

    def FindEqualAttributes(self, similarities, attributes, objectList, problem, counter, score, i):

        item = str(i)
        figurei = problem.figures[item]
        possAnswerObject = figurei
   
        for j in objectList:
            for k in range(len(similarities[str(j.name) + ', ' + item])):
                figureCName = similarities[str(j.name) + ', ' + item][k][0]
                possAnswerObjectName = similarities[str(j.name) + ', ' + item][k][1]
                objectC = j.objects[str(figureCName)]
                possAnswerObject = problem.figures[item].objects[str(possAnswerObjectName)]

                for k in range(len(attributes)):
                    attributeName = attributes[k]
                    if attributeName in objectC.attributes and attributeName in possAnswerObject.attributes:
                        if possAnswerObject.attributes[attributeName] == objectC.attributes[attributeName]:
                            score += counter.value

                    if k < len(attributes) - 1:
                        attributeName1 = attributes[k + 1]
                        if attributeName in objectC.attributes and attributeName in possAnswerObject.attributes and attributeName1 in objectC.attributes and attributeName1 in possAnswerObject.attributes:
                            if possAnswerObject.attributes[attributeName] == objectC.attributes[attributeName] and possAnswerObject.attributes[attributeName1] == objectC.attributes[attributeName1]:
                                score += counter.value * 10

        return score
