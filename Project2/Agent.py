3
# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
# PIL import Image
import random
from SemanticNet import SemanticNet
from Weights import Weights



class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.


    def Solve(self, problem):
        figureA = problem.figures['A']
        figureB = problem.figures['B']
        figureC = problem.figures['C']


        answer = -1

        attributes = {'size': 10, 'shape': 15, 'fill': 5, 'angle': 5, 'alignment': 4, 'above': 4, 'inside': 4,
                      'left-of': 4}

        
        if problem.problemType == "2x2":
           
            similarities = {}  

            similarities = Agent.GetSimilarities(self, figureA, figureB, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureA, figureC, similarities, attributes)
            for x in range(1, 7):
                possibleAnswer = problem.figures[str(x)]
                similarities = Agent.GetSimilarities(self, figureB, possibleAnswer, similarities, attributes)
                similarities = Agent.GetSimilarities(self, figureC, possibleAnswer, similarities, attributes)


            answer = self.GetTransformations(figureA, figureB, figureC, similarities, problem, problem.problemType)



        elif problem.problemType == "3x3":

            similarities = {}  

            figureD = problem.figures['D']
            figureE = problem.figures['E']
            figureF = problem.figures['F']
            figureG = problem.figures['G']
            figureH = problem.figures['H']

            similarities = Agent.GetSimilarities(self, figureA, figureC, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureA, figureG, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureA, figureB, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureB, figureC, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureD, figureE, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureE, figureF, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureG, figureH, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureA, figureD, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureD, figureG, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureB, figureE, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureE, figureH, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureC, figureF, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureC, figureG, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureC, figureE, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureE, figureG, similarities, attributes)
            similarities = Agent.GetSimilarities(self, figureA, figureE, similarities, attributes)

            figureList = [figureA,figureB,figureC,figureD,figureE,figureF,figureG,figureH]
          
            for x in range(1,9):
                possibleAnswer = problem.figures[str(x)]     
                similarities = Agent.GetSimilarities(self, figureC, possibleAnswer, similarities, attributes)
                similarities = Agent.GetSimilarities(self, figureG, possibleAnswer, similarities, attributes)
                similarities = Agent.GetSimilarities(self, figureF, possibleAnswer, similarities, attributes)
                similarities = Agent.GetSimilarities(self, figureH, possibleAnswer, similarities, attributes) 
                similarities = Agent.GetSimilarities(self, figureA, possibleAnswer, similarities, attributes)
                similarities = Agent.GetSimilarities(self, figureE, possibleAnswer, similarities, attributes)
            answer = self.Get3x3Transformations(figureA,figureB,figureC,figureD,figureE,figureF,figureG,figureH,similarities,problem)




        return answer



    def Get3x3Transformations(self, figureA, figureB, figureC,figureD, figureE, figureF,figureG,figureH,similarities, problem):
            transformations = {}
            bestPossibleAnswer = 0
            self.GetSemanticComparison(figureA, figureC, 'ac', transformations, similarities)
            self.GetSemanticComparison(figureA, figureB, 'ab', transformations, similarities)
            self.GetSemanticComparison(figureB, figureC, 'bc', transformations, similarities)
            self.GetSemanticComparison(figureD, figureE, 'de', transformations, similarities)
            self.GetSemanticComparison(figureE, figureF, 'ef', transformations, similarities)
            self.GetSemanticComparison(figureG, figureH, 'gh', transformations, similarities)
            self.GetSemanticComparison(figureA, figureG, 'ag', transformations, similarities)
            self.GetSemanticComparison(figureA, figureD, 'ad', transformations, similarities)
            self.GetSemanticComparison(figureD, figureG, 'dg', transformations, similarities)
            self.GetSemanticComparison(figureB, figureE, 'be', transformations, similarities)
            self.GetSemanticComparison(figureE, figureH, 'eh', transformations, similarities)
            self.GetSemanticComparison(figureC, figureF, 'cf', transformations, similarities)
            self.GetSemanticComparison(figureC, figureG, 'cg', transformations, similarities)
            self.GetSemanticComparison(figureC, figureE, 'ce', transformations, similarities)
            self.GetSemanticComparison(figureE, figureG, 'eg', transformations, similarities)
            self.GetSemanticComparison(figureA, figureE, 'ae', transformations, similarities)
            
            for i in range(1, 9):     # i = figureAnswer
                figureAnswer = problem.figures[str(i)]
                similarityScore = 0   
                semanticNet = SemanticNet()

                similarityScore = semanticNet.FindDeletedObjects(figureA, figureC, figureG, figureAnswer, 'ac', 'gi', problem, similarityScore, transformations, i)
                similarityScore = semanticNet.FindDeletedObjects(figureE, figureF, figureH, figureAnswer, 'ef', 'hi', problem, similarityScore,transformations, i)
                similarityScore = semanticNet.FindDeletedObjects(figureA, figureG, figureC, figureAnswer, 'ag', 'ci', problem, similarityScore, transformations, i)
                similarityScore = semanticNet.FindDeletedObjects(figureE, figureH, figureF, figureAnswer, 'eh', 'fi', problem, similarityScore,transformations, i)
                similarityScore = self.GetScore(figureG, problem, i, 'ac', 'gi', similarityScore,transformations, similarities,semanticNet)
                similarityScore = self.GetScore(figureH, problem, i, 'bc', 'hi', similarityScore,transformations, similarities,semanticNet)
                similarityScore = self.GetScore(figureH, problem, i, 'gh', 'hi', similarityScore,transformations, similarities,semanticNet)
                similarityScore = self.GetScore(figureC, problem, i, 'ag', 'ci', similarityScore,transformations, similarities,semanticNet)
                similarityScore = self.GetScore(figureF, problem, i, 'dg', 'fi', similarityScore,transformations, similarities,semanticNet)
                similarityScore = self.GetScore(figureF, problem, i, 'cf', 'fi', similarityScore,transformations, similarities,semanticNet)
                similarityScore = self.GetScore(figureA, problem, i, 'cg', 'ai', similarityScore,transformations, similarities,semanticNet)
                similarityScore = self.GetScore(figureE, problem, i, 'ae', 'ei', similarityScore,transformations, similarities,semanticNet)
                objectList = [figureA, figureC, figureF, figureG, figureH]               
                attributes = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of'] 


                similarityScore = semanticNet.FindEqualAttributes(similarities, attributes, objectList, problem, Weights.counter, similarityScore,i)
                if similarityScore is not None:
                    if similarityScore > bestPossibleAnswer:
                        bestPossibleAnswer = similarityScore
                        answer = i

                    elif similarityScore == bestPossibleAnswer:
                        if random.randint(0, 1) == 0:
                            bestPossibleAnswer = similarityScore
                            answer = i
            return answer 




   
    def GetTransformations(self, figureA, figureB, figureC, similarities, problem, problemType):
    
        transformations = {}

        if problemType == "2x2":
            self.GetSemanticComparison(figureA, figureB, 'ab', transformations, similarities)
            self.GetSemanticComparison(figureA, figureC, 'ac', transformations, similarities)
            bestPossibleAnswer = 0


            for i in range(1, 7):
                figureD = problem.figures[str(i)]
                similarityScore = 0
                semanticNet = SemanticNet()

                similarityScore = semanticNet.FindDeletedObjects(figureA, figureB, figureC, figureD, 'ab', 'cd', problem, similarityScore, transformations, i)


                similarityScore = semanticNet.FindDeletedObjects(figureA, figureC, figureB, figureD, 'ac', 'bd', problem, similarityScore,transformations, i)

                similarityScore = self.GetScore(figureC, problem, i, 'ab', 'cd', similarityScore,transformations, similarities, semanticNet)

                similarityScore = self.GetScore(figureB, problem, i, 'ac', 'bd', similarityScore,transformations, similarities,semanticNet)


                attributes = ['size', 'shape']
                objectList = [figureB, figureC]
                similarityScore = semanticNet.FindEqualAttributes(similarities, attributes, objectList, problem, Weights.counter, similarityScore,i)
                if similarityScore is not None:
                    if similarityScore > bestPossibleAnswer:
                        bestPossibleAnswer = similarityScore
                        answer = i

                    elif similarityScore == bestPossibleAnswer:
                       answer = self.GetTieBreaker(similarityScore, i)
            return answer    
       

    def GetTieBreaker(self, similarityScore, i):
        if random.randint(0, 1) == 1:
            bestPossibleAnswer = similarityScore
            answer = i
            return answer
        else:
            return 1



  

    def GetSemanticComparison(self, figureA, figureB, attribute, transformations, similarities):

        semanticNet = SemanticNet()
        for i in range(len(similarities[str(figureA.name) + ', ' + str(figureB.name)])):
            figureItem = str(i)
            objectAName  = similarities[str(figureA.name) + ', ' + str(figureB.name)][i][0]
            objectBName =  similarities[str(figureA.name) + ', ' + str(figureB.name)][i][1]
            objectA = figureA.objects[str(objectAName)]
            objectB = figureB.objects[str(objectBName)]

            self.PerformConvertCompare(objectA,objectB,i,transformations,attribute,semanticNet)

            if 'angle' in objectA.attributes and 'angle' in objectB.attributes:
                  transformations[figureItem + attribute + 'AngleDifference'] = int(objectA.attributes['angle']) - int(objectB.attributes['angle'])


            if objectA.attributes['fill'] == objectB.attributes['fill']:
                self.FillComparison(objectA, objectB, attribute, figureItem, transformations, True)
            if 'alignment' in objectA.attributes and 'alignment' in objectB.attributes:
                 if objectA.attributes['alignment'] != objectB.attributes['alignment']:
                    transformations[figureItem + attribute + 'AlignDifference'] = objectA.attributes['alignment'] + '-' + objectB.attributes['alignment']
                    transformations[figureItem + attribute + 'AlignDifference'] = semanticNet.EliminDuplicates(transformations[figureItem + attribute + 'AlignDifference'])





            elif objectA.attributes['fill'] == 'no' and objectB.attributes['fill'] == 'yes':
                transformations[figureItem + attribute + 'FillDifference'] = 1
            elif objectA.attributes['fill'] == 'yes' and objectB.attributes['fill'] == 'no':
                self.FillComparison(objectA, objectB, attribute, figureItem, transformations, False)

    def PerformConvertCompare(self, objectA,objectB,i,transformations,attribute,semanticNet):
            semanticNet.ConvertShape(objectA,objectB)
            transformations = semanticNet.CompareObjects(objectA, objectB, i, transformations, attribute)

            transformations[str(i) + attribute + 'ShapeDifference'] = (objectA.attributes['shape'] + '-' + objectB.attributes['shape'])

            semanticNet.CompareAttributes(objectA, objectB, i, transformations, attribute, 'overlaps')
            semanticNet.CompareAttributes(objectA, objectB, i, transformations, attribute, 'overlapCondition')
            semanticNet.CompareAttributes(objectA, objectB, i, transformations, attribute, 'left-of')
            semanticNet.CompareAttributes(objectA, objectB, i, transformations, attribute, 'above')
            semanticNet.CompareAttributes(objectA, objectB, i, transformations, attribute, 'size')


    def FillComparison(self,objectA, objectB, attribute, figureItem, transformations, switch):
        if switch:
            transformations[figureItem + attribute + 'FillDifference'] = 0
        else:
            transformations[figureItem + attribute + 'FillDifference'] = -1
        return transformations




    def GetScore(self, figureC, problem, i, objectNameList, objectNameList1,score, transformations, similarities, semanticNet):

        possibleAnswer = problem.figures[str(i)]

        for j in range(len(similarities[str(figureC.name) + ', ' + str(i)])):
            objectCname = similarities[str(figureC.name) + ', ' + str(i)][j][0]
            possibleAnsName = similarities[str(figureC.name) + ', ' + str(i)][j][1]
            objectC = figureC.objects[str(objectCname)]
            objectAnswer = possibleAnswer.objects[possibleAnsName]

            score = semanticNet.CalculateTransformScore(j, score, transformations, objectNameList, objectNameList1, 'overlap',Weights.overlapsWeightCtr.value)
            score = semanticNet.CalculateTransformScore(j, score, transformations, objectNameList, objectNameList1, 'overlapCondition',Weights.overlapsWeightCtr.value)
            score = semanticNet.CalculateTransformScore(j, score, transformations, objectNameList, objectNameList1, 'left-of',Weights.leftOfWeight.value)
            score = semanticNet.CalculateTransformScore(j, score, transformations, objectNameList, objectNameList1, 'above', Weights.aboveWeight.value)
            semanticNet.ConvertShape(objectC, objectAnswer)
            score = semanticNet.CalculateTransformScore(j, score, transformations, objectNameList, objectNameList1, 'height', Weights.sizeWeight.value)
            score = semanticNet.CalculateTransformScore(j, score, transformations, objectNameList, objectNameList1, 'width', Weights.sizeWeight.value)

          
            transformations = semanticNet.CompareObjects(objectC, objectAnswer, j, transformations, objectNameList1)


            transformations[str(j) + objectNameList1 + 'ShapeDifference'] = (objectC.attributes['shape'] + '-' + objectAnswer.attributes['shape'])



            if str(j) + objectNameList + 'ShapeDifference' in transformations and str(j) + objectNameList1 + 'ShapeDifference' in transformations:
               
                if (transformations[str(j) + objectNameList + 'ShapeDifference']) == (
                        transformations[str(j) + objectNameList1 + 'ShapeDifference']):
                    score += Weights.shapeWeight.value


            score = semanticNet.CalculateTransformScore(j, score, transformations, objectNameList, objectNameList1, 'size', Weights.sizeWeight.value)

            if 'angle' in objectC.attributes and 'angle' in objectAnswer.attributes: 
                transformations[str(j) + objectNameList1 + 'AngleDifference'] = int(objectC.attributes['angle']) - int(
                    objectAnswer.attributes['angle'])



            if str(j) + objectNameList + 'AngleDifference' in transformations and str(j) + objectNameList1 + 'AngleDifference' in transformations:
                if abs(transformations[str(j) + objectNameList + 'AngleDifference'] + 180) % 360 == abs(
                        transformations[str(j) + objectNameList1 + 'AngleDifference']):
                    score += Weights.reflectionWeight.value

                elif transformations[str(j) + objectNameList + 'AngleDifference'] == transformations[str(j) + objectNameList1 + 'AngleDifference']:
                    score += Weights.angleWeight.value


            if 'alignment' in objectC.attributes and 'alignment' in objectAnswer.attributes:
                if objectC.attributes['alignment'] != objectAnswer.attributes['alignment']:
                    transformations[str(j) + objectNameList1 + 'AlignDifference'] = objectC.attributes['alignment'] + '-' + objectAnswer.attributes['alignment']


                    transformations[str(j) + objectNameList1 + 'AlignDifference'] = semanticNet.EliminDuplicates(transformations[str(j) + objectNameList1 + 'AlignDifference'])


                if (str(j) + objectNameList + 'AlignDifference') in transformations and (
                        str(j) + objectNameList1 + 'AlignDifference') in transformations:
                    if (transformations[str(j) + objectNameList + 'AlignDifference']) == (
                            transformations[str(j) + objectNameList1 + 'AlignDifference']) and transformations[
                        str(j) + objectNameList + 'AlignDifference'] != 'empty-' and transformations[
                        str(j) + objectNameList1 + 'AlignDifference'] != 'empty-':
                        score += Weights.alignWeight.value


            possAnswer = objectAnswer.attributes['fill']
            if objectC.attributes['fill'] == possAnswer:
                transformations[str(j) + objectNameList1 + 'FillDifference'] = 0
            else:
                transformations[str(j) + objectNameList1 + 'FillDifference'] = 1
              
            if str(j) + objectNameList + 'FillDifference' in transformations and str(j) + objectNameList1 + 'FillDifference' in transformations:
                if transformations[str(j) + objectNameList + 'FillDifference'] == transformations[str(j) + objectNameList1 + 'FillDifference']:
                    score += Weights.fillWeight.value

            


        return score



    def GetSimilarities(self, figure1, figure2, similarities, attributes):

        temp = []
        weightList = list(attributes.values())
        attributeListKeys = list(attributes.keys())
        similarityList = []
       

        if len(figure2.objects) < len(figure1.objects):

            for objectName1 in sorted(figure1.objects):
                object1 = figure1.objects[objectName1]
                temp.append(object1)

            for objectName2 in sorted(figure2.objects):
                objectMaxScore = 0
                object2 = figure2.objects[objectName2]
                objectTopScore = None

                for object1 in temp:
                    similarityCount = 0
                    for i in range(len(attributes)):
                        attributeName = attributeListKeys[i]
                        counter = weightList[i]
                        if attributeName in object1.attributes and attributeName in object2.attributes:
                            if object1.attributes[attributeName] == object2.attributes[attributeName]:
                                similarityCount += counter
                        if i < len(attributes) - 1:
                            attributeName1 = attributeListKeys[i + 1]
                            counter2 = weightList[i + 1]
                            if attributeName in object1.attributes and attributeName in object2.attributes and attributeName1 in object1.attributes and attributeName1 in object2.attributes:
                                if object2.attributes[attributeName] == object1.attributes[attributeName] and object2.attributes[attributeName1] == object1.attributes[attributeName1]:
                                    similarityCount += (counter + counter2) * 2

                    if similarityCount > objectMaxScore:
                        objectMaxScore = similarityCount
                        objectTopScore = object1


                if objectTopScore is not None:
                    similarityList.append((objectTopScore.name, object2.name))
                    temp.remove(objectTopScore)


        elif len(figure2.objects) >= len(figure1.objects):

            for objectName2 in sorted(figure2.objects):
                temp.append(figure2.objects[objectName2])

            for objectName1 in sorted(figure1.objects):
                object1 = figure1.objects[objectName1]
                objectTopScore = None
                objectMaxScore = 0
                for object2 in temp:
                    similarityCount = 0

                    for i in range(len(attributes)):
                        attributeName = attributeListKeys[i]
                        counter = weightList[i]
                        if attributeName in object1.attributes and attributeName in object2.attributes:
                            if object1.attributes[attributeName] == object2.attributes[attributeName]:
                                similarityCount += counter

                        if i < len(attributes) - 1:
                            attributeName1 = attributeListKeys[i + 1]
                            counter2 = weightList[i + 1]
                            if attributeName in object1.attributes and attributeName in object2.attributes and attributeName1 in object1.attributes and attributeName1 in object2.attributes:
                                if object2.attributes[attributeName] == object1.attributes[attributeName] and object2.attributes[attributeName1] == object1.attributes[attributeName1]:
                                    similarityCount += (counter + counter2) * 3

                    if similarityCount > objectMaxScore:
                        objectMaxScore = similarityCount
                        objectTopScore = object2


                if objectTopScore is not None:
                    similarityList.append((object1.name, objectTopScore.name))
                    temp.remove(objectTopScore)

         
        similarities[str(figure1.name) + ', ' + str(figure2.name)] = similarityList

        return similarities



    

   




   

