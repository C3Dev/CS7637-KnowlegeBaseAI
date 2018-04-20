__author__ = 'Daniel Rozen'

import random


def Project2Solve(self, problem):

    # Define figure variables

    p1 = problem.figures['1']
    p2 = problem.figures['2']
    p3 = problem.figures['3']
    p4 = problem.figures['4']
    p5 = problem.figures['5']
    p6 = problem.figures['6']

    a = problem.figures['A']
    b = problem.figures['B']
    c = problem.figures['C']

    maxTot = 0   # initiate a best answer score variable to 0
    answer = -1   # initialize best answer response to skip

    # Define increment variables (Adjustable)
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

    # Setup matching objects dictionary:
    matchObjsDict = {} # dictionary to match objects
    # attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of']
    attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of'] # list of attributes used to match objects
    incrList = [10, 15, 5, 5, 4, 4, 4, 4] # corresponding attribute weights

    if problem.name == 'Basic Problem C-06':
        print('Set Breakpoint here!')

    if problem.problemType == "2x2":
        #  loop through all objects and add to dictionary

        matchObjsDict = matchObjects(self, a, b, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, a, c, matchObjsDict, attributeList, incrList)
        for x in range(1,7):
            ans = problem.figures[str(x)]
            matchObjsDict = matchObjects(self, b, ans, matchObjsDict, attributeList, incrList)
            matchObjsDict = matchObjects(self, c, ans, matchObjsDict, attributeList, incrList)

        print("\n" + problem.name + "\n")

        # print('\nOBJECT MATCHING DICTIONARY!')
        # for keys in sorted(matchObjsDict):
        #     print(str(keys) + ": " + str(matchObjsDict[keys]))

    # compare shapes and attributes across figures A,B,C:

        transformDict = {}  # create dictionary for transformations

        # compare A to B
        compareAtoObj(self, a, b, 'ab', transformDict, matchObjsDict)
        # # compare A to C
        compareAtoObj(self, a, c, 'ac', transformDict, matchObjsDict)
        # comparing  figures to answers
        for x in range(1, 7):     # loop through each potential answer from 1 to 6:

            d = problem.figures[str(x)]

            print('\n  Now comparing answer: ' + str(x) + ' to ' + problem.name + ':\n')

            tot = 0   # initialize total points system

            initialize_dicts(self, transformDict) # initialize empty keys in transformation dicts

            # compare deletion from AB to CD
            tot = abcd_delete_comp(self, a, b, c, d, 'ab', 'cd', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

            # compare deletion from AC to BD

            tot = abcd_delete_comp(self, a, c, b,  d, 'ac', 'bd', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

            # compare C to D
            tot = compareObjtoAns(self, c, problem, x, 'ab', 'cd', alignIncr, angleIncr, fillIncr,
                                        reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)
            # # compare B to D
            tot = compareObjtoAns(self, b, problem, x, 'ac', 'bd', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)

            # compare remaining attributes to answer
            # attributeList = ['size', 'shape', 'fill', 'alignment', 'angle', 'above', 'inside']
            attributeList = ['size', 'shape']
            objCompareList = [b, c]
            tot = compEqAttributes(self, matchObjsDict, attributeList, objCompareList, problem, sameIncr, tot, x)

            # if local answer > max answer:
            print("current answer " + str(x) + ' total = ' + str(tot) + ' MaxTotal = ' + str(maxTot))

            if tot is not None:
                if tot > maxTot:
                    # max answer = local answer
                    print("previous maxTot = " + str(maxTot))
                    maxTot = tot
                    print("new maxTot = " + str(maxTot))
                    # answer = current answer
                    print("previous answer = " + str(answer))

                    answer = x

                    print("new answer = " + str(answer))

                elif tot == maxTot: #random tie breaker
                        if random.randint(0,1) == 1:
                            print("previous maxTot = " + str(maxTot))
                            maxTot = tot
                            print("new maxTot = " + str(maxTot))
                            # answer = current answer
                            print("previous answer = " + str(answer))
                            answer = x
                            print("new answer = " + str(answer))

        print("final answer = " + str(answer))

        return answer

# -------------------------------------------------------------------------------------------------------
    # FOR 3X3 check if problem type is 3x3

    elif problem.problemType == "3x3":

        a = problem.figures['A']
        b = problem.figures['B']
        c = problem.figures['C']
        # define extra figure objects

        d = problem.figures['D']
        e = problem.figures['E']
        f = problem.figures['F']
        g = problem.figures['G']
        h = problem.figures['H']

        # Setup matching objects dictionary:
        matchObjsDict = {} # dictionary to match objects
        # attributeList = ['size', 'shape', 'fill'] # list of attributes used to match objects
        # incrList = [5, 10, 5] # corresponding attribute weights
        # attributeList = ['size', 'shape', 'fill', 'angle', 'alignment'] # list of attributes used to match objects
        attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of'] # list of attributes used to match objects
        incrList = [10, 15, 5, 5, 4, 4, 4, 4] # corresponding attribute weights

        # loop through all objects and add to dictionary
        #print('Now Matching problem: ' + problem.name)
        #print('Now Matching objects ' + a.name + ' and ' + c.name + ' for ' + problem.name )

        matchObjsDict = matchObjects(self, a, c, matchObjsDict, attributeList, incrList)

        matchObjsDict = matchObjects(self, a, g, matchObjsDict, attributeList, incrList)

        # extra comparisons:

        # Horizontal comparisons
        matchObjsDict = matchObjects(self, a, b, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, b, c, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, d, e, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, e, f, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, g, h, matchObjsDict, attributeList, incrList)

        # Vertical comparisons
        matchObjsDict = matchObjects(self, a, d, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, d, g, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, b, e, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, e, h, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, c, f, matchObjsDict, attributeList, incrList)

        # Diagonal comparisons
        matchObjsDict = matchObjects(self, c, g, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, c, e, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, e, g, matchObjsDict, attributeList, incrList)
        matchObjsDict = matchObjects(self, a, e, matchObjsDict, attributeList, incrList)

        # add overlaps boolean
        figureList = [a,b,c,d,e,f,g,h]
        for figure in figureList:
            addOverlapsBoolean(self, figure) # add overlaps boolean
            # attributeList = ['left-of', 'above', 'inside'] # add opposite attributes

            # attributeList = ['left-of', 'above'] # add opposite attributes
            # for attribute in attributeList:
            #     convertOppositeAttributes(figure, attribute)

        for x in range(1,9):
            ans = problem.figures[str(x)]
            addOverlapsBoolean(self, ans)             # add overlaps boolean
            matchObjsDict = matchObjects(self, c, ans, matchObjsDict, attributeList, incrList)
            matchObjsDict = matchObjects(self, g, ans, matchObjsDict, attributeList, incrList)

            # extra comparisons:
            matchObjsDict = matchObjects(self, f, ans, matchObjsDict, attributeList, incrList)
            matchObjsDict = matchObjects(self, h, ans, matchObjsDict, attributeList, incrList)
            # Diagonal comparisons
            matchObjsDict = matchObjects(self, a, ans, matchObjsDict, attributeList, incrList)
            matchObjsDict = matchObjects(self, e, ans, matchObjsDict, attributeList, incrList)

        print("\n" + problem.name + "\n")

        # print('\nOBJECT MATCHING DICTIONARY!')
        # for keys in sorted(matchObjsDict):
        #     print(str(keys) + ": " + str(matchObjsDict[keys]))

        transformDict = {}  # create dictionary for transformations

        # compare shapes and attributes across figures A,B,C:

        # Compare Horizontally:
        # compare A to C
        compareAtoObj(self, a, c, 'ac', transformDict, matchObjsDict)
        compareAtoObj(self, a, b, 'ab', transformDict, matchObjsDict)
        compareAtoObj(self, b, c, 'bc', transformDict, matchObjsDict)
        compareAtoObj(self, d, e, 'de', transformDict, matchObjsDict)
        compareAtoObj(self, e, f, 'ef', transformDict, matchObjsDict)
        compareAtoObj(self, g, h, 'gh', transformDict, matchObjsDict)

        # Compare Vertically:
        # # compare A to G
        compareAtoObj(self, a, g, 'ag', transformDict, matchObjsDict)
        compareAtoObj(self, a, d, 'ad', transformDict, matchObjsDict)
        compareAtoObj(self, d, g, 'dg', transformDict, matchObjsDict)
        compareAtoObj(self, b, e, 'be', transformDict, matchObjsDict)
        compareAtoObj(self, e, h, 'eh', transformDict, matchObjsDict)
        compareAtoObj(self, c, f, 'cf', transformDict, matchObjsDict)

        # Diagonal comparisons
        compareAtoObj(self, c, g, 'cg', transformDict, matchObjsDict)
        compareAtoObj(self, c, e, 'ce', transformDict, matchObjsDict)
        compareAtoObj(self, e, g, 'eg', transformDict, matchObjsDict)
        compareAtoObj(self, a, e, 'ae', transformDict, matchObjsDict)

        for x in range(1, 9):     # loop through each potential answer from 1 to 8:
            if x == 7:
                print('set breakpoint here')
            i = problem.figures[str(x)]

            print('\n  Now comparing answer: ' + str(x) + ' to ' + problem.name + ':\n')
            tot = 0   # initialize

            initialize_dicts(self, transformDict) # initialize empty keys in transformation dicts

            # compare deletion from AC to GAns

            tot = abcd_delete_comp(self, a, c, g, i, 'ac', 'gi', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)
            tot = abcd_delete_comp(self, e, f, h, i, 'ef', 'hi', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

            # compare deletion from AG to CAns
            tot = abcd_delete_comp(self, a, g, c, i, 'ag', 'ci', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)
            tot = abcd_delete_comp(self, e, h, f, i, 'eh', 'fi', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

            # diagonals
            # tot = abcd_delete_comp(c, g, a, i, 'cg', 'ai', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)
            # tot = abcd_delete_comp(f, h, e, i, 'fh', 'ai', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

            # for ansObjName in sortDict(problem.figures[str(x)].objects):
            #     ansObj = problem.figures[str(x)].objects[ansObjName]


            # Horizontal
            # compare G to I
            tot = compareObjtoAns(self, g, problem, x, 'ac', 'gi', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)
            tot = compareObjtoAns(self, h, problem, x, 'bc', 'hi', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)
            tot = compareObjtoAns(self, h, problem, x, 'gh', 'hi', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)

            # tot = compareObjtoAns(self, h, problem, x, 'ef', 'hi', alignIncr, angleIncr, fillIncr,
            #                            reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
            #                            transformDict, matchObjsDict)

            # Vertical

            # # compare C to I
            tot = compareObjtoAns(self, c, problem, x, 'ag', 'ci', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)

            tot = compareObjtoAns(self, f, problem, x, 'dg', 'fi', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)

            tot = compareObjtoAns(self, f, problem, x, 'cf', 'fi', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)
            #
            # tot = compareObjtoAns(f, problem, x, 'eh', 'fi', alignIncr, angleIncr, fillIncr,
            #                            reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
            #                            transformDict, matchObjsDict)


            # Diagonal comparisons

            tot = compareObjtoAns(self, a, problem, x, 'cg', 'ai', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)

            tot = compareObjtoAns(self, e, problem, x, 'ae', 'ei', alignIncr, angleIncr, fillIncr,
                                       reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
                                       transformDict, matchObjsDict)

            # tot = compareObjtoAns(e, problem, x, 'fh', 'ei', alignIncr, angleIncr, fillIncr,
            #                            reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr, tot,
            #                            transformDict, matchObjsDict)

            # compare remaining attributes to answer
            objCompareList = [a, c, f, g, h]
            # attributeList = ['size', 'shape', 'fill', 'alignment', 'angle', 'above', 'inside']
            attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of'] # list of attributes used to match objects
            incrList = [10, 15, 5, 5, 4, 4, 4, 4] # corresponding attribute weights

            tot = compEqAttributes(self, matchObjsDict, attributeList, objCompareList, problem, sameIncr, tot, x)

            print('Current Total: ' + str(tot) + ' for Answer: ' + str(x) + ' maxTot = ' + str(maxTot))
            # if local answer > max answer:
            if tot is not None:
                if tot > maxTot:
                    # max answer = local answer
                    print("previous maxTot = " + str(maxTot))
                    maxTot = tot
                    print("new maxTot = " + str(maxTot))
                    # answer = current answer
                    print("previous answer = " + str(answer))
                    answer = x
                    print("new answer = " + str(answer))
                elif tot == maxTot: #random tie breaker
                    if random.randint(0,1) == 0:
                        print("previous maxTot = " + str(maxTot))
                        maxTot = tot
                        print("new maxTot = " + str(maxTot))
                        # answer = current answer
                        print("previous answer = " + str(answer))
                        answer = x
                        print("new answer = " + str(answer))

        print("final answer = " + str(answer))

        return answer

# Helpful Functions:

# From Project 2:

def initialize_dicts(self, transformDict):
    # initialize empty keys for angle transformations
    transformDict['abAngleDiff'] = None
    transformDict['cdAngleDiff'] = None
    transformDict['acAngleDiff'] = None
    transformDict['bdAngleDiff'] = None
    # initialize empty keys for fill transformations
    transformDict['abFillDiff'] = None
    transformDict['cdFillDiff'] = None
    transformDict['acFillDiff'] = None
    transformDict['bdFillDiff'] = None
    # initialize empty keys for shape transformations
    transformDict['abShapeDiff'] = ''
    transformDict['cdShapeDiff'] = ''
    transformDict['acShapeDiff'] = ''
    transformDict['bdShapeDiff'] = ''
    # initialize empty keys for size transformations
    transformDict['abSizeDiff'] = 0
    transformDict['cdSizeDiff'] = 0
    transformDict['acSizeDiff'] = 0
    transformDict['bdSizeDiff'] = 0
    # initialize empty keys for alignment transformations
    transformDict['abAlignDiff'] = 'empty-'
    transformDict['cdAlignDiff'] = 'empty-'
    transformDict['acAlignDiff'] = 'empty-'
    transformDict['bdAlignDiff'] = 'empty-'

# def acbd_delete_comp(self, a, c, deleteIncr, g, varNames, varNames1, problem, tot, transformDict, x):
#     transformDict[varNames + 'DeleteDiff'] = len(a.objects) - len(g.objects)
#     print(varNames + 'DeleteDiff: ' + str(transformDict[varNames + 'DeleteDiff']))
#     transformDict[varNames1 + 'DeleteDiff'] = len(c.objects) - len(problem.figures[str(x)].objects)
#     print(varNames1 + 'DeleteDiff: ' + str(transformDict[varNames1 + 'DeleteDiff']))
#     if transformDict[varNames + 'DeleteDiff'] == transformDict[varNames1 + 'DeleteDiff']:
#         tot += (deleteIncr * transformDict[varNames + 'DeleteDiff'])
#         # tot += (deleteIncr)
#         print('AC BD same deletion!')
#
#     return tot

def abcd_delete_comp(self, a, b, c, ans, varNames, varNames1, deleteIncr, deleteCompIncr, problem, tot, transformDict, x):

    if a is None:
        aLen = 0
    else:
        aLen = len(a.objects)
    if b is None:
        bLen = 0
    else:
        bLen = len(b.objects)
    if c is None:
        cLen = 0
    else:
        cLen = len(c.objects)
    if ans is None:
        ansLen = 0
    else:
        ansLen = len(problem.figures[str(x)].objects)

    transformDict[varNames + 'DeleteDiff'] = aLen - bLen
    # print(varNames + 'DeleteDiff: ' + str(transformDict[varNames + 'DeleteDiff']))
    transformDict[varNames1 + 'DeleteDiff'] = cLen - ansLen
    # print(varNames1 + 'DeleteDiff: ' + str(transformDict[varNames1 + 'DeleteDiff']))

    if transformDict[varNames + 'DeleteDiff'] == transformDict[varNames1 + 'DeleteDiff'] and transformDict[varNames + 'DeleteDiff'] != 0:
        # total is increased by increments x # deletions
        tot += (deleteIncr * abs(transformDict[varNames + 'DeleteDiff']))
        # tot += (deleteIncr)
        print('AB CD same deletion!')
    elif transformDict[varNames + 'DeleteDiff'] == transformDict[varNames1 + 'DeleteDiff'] and transformDict[varNames + 'DeleteDiff'] == 0:
        tot += deleteIncr
        print('AB CD same NO deletion!')
    else: # non-zero unequal values
        if aLen != 0 and bLen != 0 and cLen != 0 and ansLen != 0:
            transformDict[varNames + 'DeleteMultDiff'] = float(bLen)/aLen
            transformDict[varNames1 + 'DeleteMultDiff'] = float(ansLen)/cLen
            if transformDict[varNames + 'DeleteMultDiff'] == transformDict[varNames1 + 'DeleteMultDiff']:
                tot += deleteIncr * 2
                print("CORRECT " + 'DeleteMultDiff' + " TRANSFORM FOR " + varNames + varNames1)
    # Compensate for deletion
    if ansLen < min(aLen, bLen, cLen):
        tot += (min(aLen, bLen, cLen) - ansLen) * deleteCompIncr
        print('Object Deletion compensation of ' + str(min(aLen, bLen, cLen) - ansLen) + ' objects. Tot = ' + str(tot))
    elif ansLen > max(aLen, bLen, cLen):
        tot += (ansLen - max(aLen, bLen, cLen)) * deleteCompIncr
        print('Object Addition compensation of ' + str(min(aLen, bLen, cLen) - ansLen) + ' objects. Tot = ' + str(tot))
    return tot

def compEqAttributes(self, matchObjsDict, attributeList, objCompareList, problem, sameIncr, tot, x):

    ansObj = problem.figures[str(x)]
    # todo: choose min of the 2

    for c in objCompareList:
        for n in range(len(matchObjsDict[str(c.name) + ', ' + str(x)])):
            cObjName, ansObjName = matchObjsDict[str(c.name) + ', ' +str(x)][n][0], matchObjsDict[str(c.name) + ', ' +str(x)][n][1]
            cObj, ansObj = c.objects[str(cObjName)], problem.figures[str(x)].objects[str(ansObjName)]

            for n in range(len(attributeList)):
                attributeName = attributeList[n]
                if attributeName in cObj.attributes and attributeName in ansObj.attributes:
                    if ansObj.attributes[attributeName] == cObj.attributes[attributeName]:
                        tot += sameIncr

                # compare multiple attributes at the same time!
                if n < len(attributeList)-1:
                    attributeName1 = attributeList[n+1]
                    if attributeName in cObj.attributes and attributeName in ansObj.attributes and attributeName1 in cObj.attributes and attributeName1 in ansObj.attributes:
                        if ansObj.attributes[attributeName] == cObj.attributes[attributeName] and ansObj.attributes[attributeName1] == cObj.attributes[attributeName1]:
                            tot += sameIncr * 10
                        # print('Figure' + str(fig.name) + ' attrib: ' + attributeName + ' compared to ' + str(
                        #     x) + ', current total = ' + str(tot))
    return tot

def matchObjects(self, fig1, fig2, matchObjsDict, attributeList, incrList):

    # Todo: create deleted objects

    candidateObjsList = [] # candidate object of fig2 list, will be removed once matched

    matchObjsList = []

    if len(fig2.objects) >= len(fig1.objects):

        for obj2Name in sorted(fig2.objects):
            candidateObjsList.append(fig2.objects[obj2Name])

        for obj1Name in sorted(fig1.objects):
            obj1 = fig1.objects[obj1Name]
            maxObj = None
            maxTot = 0
            for obj2 in candidateObjsList:
                tot = 0
                # for attributeName, incr in zip(attributeList, incrList):
                #         if attributeName in obj1.attributes and attributeName in obj2.attributes:
                #             if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                #                 tot += incr
                                # print('OBJECT MATCH! attr: ' + attributeName + ' ' + str(incr) + ' pts  New total: ' + str(tot) )
                for n in range(len(attributeList)):
                    attributeName = attributeList[n]
                    incr = incrList[n]
                    if attributeName in obj1.attributes and attributeName in obj2.attributes:
                            if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                                tot += incr
                                # print('Object attribute match ' + attributeName + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                    # compare multiple attributes at the same time!
                    if n < len(attributeList)-1:
                        attributeName1 = attributeList[n+1]
                        incr1 = incrList[n+1]
                        if attributeName in obj1.attributes and attributeName in obj2.attributes and attributeName1 in obj1.attributes and attributeName1 in obj2.attributes:
                            if obj2.attributes[attributeName] == obj1.attributes[attributeName] and obj2.attributes[attributeName1] == obj1.attributes[attributeName1]:
                                tot += (incr + incr1) * 10
                                # print('DOUBLE ATTR INCR ' + attributeName + ' and ' + attributeName1 + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                #print ('Total for objects ' + obj1Name + ' and ' + obj2.name + ' = ' + str(tot))
                if tot > maxTot:
                    maxTot = tot
                    maxObj = obj2
                    # print ('New Max Obj! ' + obj2.name + ' = ' + str(tot))

            if maxObj is not None:
                matchObjsList.append((obj1.name, maxObj.name))
                candidateObjsList.remove(maxObj)

    elif len(fig2.objects) < len(fig1.objects):

        for obj1Name in sorted(fig1.objects):
            candidateObjsList.append(fig1.objects[obj1Name])

        for obj2Name in sorted(fig2.objects):
            obj2 = fig2.objects[obj2Name]
            maxObj = None
            maxTot = 0
            for obj1 in candidateObjsList:
                tot = 0
                # for attributeName, incr in zip(attributeList, incrList):
                #         if attributeName in obj1.attributes and attributeName in obj2.attributes:
                #             if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                #                 tot += incr
                #                 #print('OBJECT MATCH! attr: ' + attributeName + ' ' + str(incr) + ' pts  New total: ' + str(tot) )
                for n in range(len(attributeList)):
                    attributeName = attributeList[n]
                    incr = incrList[n]
                    if attributeName in obj1.attributes and attributeName in obj2.attributes:
                            if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                                tot += incr
                                # print('Object attribute match ' + attributeName + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                    # compare multiple attributes at the same time!
                    if n < len(attributeList)-1:
                        attributeName1 = attributeList[n+1]
                        incr1 = incrList[n+1]
                        if attributeName in obj1.attributes and attributeName in obj2.attributes and attributeName1 in obj1.attributes and attributeName1 in obj2.attributes:
                            if obj2.attributes[attributeName] == obj1.attributes[attributeName] and obj2.attributes[attributeName1] == obj1.attributes[attributeName1]:
                                tot += (incr + incr1) * 5
                                # print('DOUBLE ATTR INCR ' + attributeName + ' and ' + attributeName1 + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                #print ('Total for objects ' + obj1Name + ' and ' + obj2.name + ' = ' + str(tot))
                if tot > maxTot:
                    maxTot = tot
                    maxObj = obj1
                    # print ('New Max Obj! ' + obj1.name + ' = ' + str(tot))

            if maxObj is not None:
                matchObjsList.append((maxObj.name, obj2.name))
                candidateObjsList.remove(maxObj)

    matchObjsDict[str(fig1.name) + ', ' +str(fig2.name)] = matchObjsList

    return matchObjsDict

def compareAtoObj(self, a, b, varNames, transformDict, matchObjsDict):

    # todo: choose min of the 2
    for n in range(len(matchObjsDict[str(a.name) + ', ' + str(b.name)])):
        aObjName, bObjName = matchObjsDict[str(a.name) + ', ' + str(b.name)][n][0], matchObjsDict[str(a.name) + ', ' +str(b.name)][n][1]
        aObj, bObj = a.objects[str(aObjName)], b.objects[str(bObjName)]

        #make special case of square having properties of height and width and compare to rectangle
        convertSquareToRectangle(self, aObj)
        convertSquareToRectangle(self, bObj)

        # compare height and width of rectangles
        compHeightAndWidth(self, aObj, bObj, n, transformDict, varNames)

        # check for shape transform:
        #if aObj.attributes['shape'] != bObj.attributes['shape']:
        transformDict[str(n) + varNames + 'ShapeDiff'] = (aObj.attributes['shape'] + '-' + bObj.attributes['shape'])
        print('\nShape Transform for ' + str(n) + varNames + ' : ' + transformDict[str(n) + varNames + 'ShapeDiff'])

        # TODO: add new transforms comparing overlaps, left-of, and above.

        compareAttribute(self, aObj, bObj, n, transformDict, varNames, 'overlaps')
        compareAttribute(self, aObj, bObj, n, transformDict, varNames, 'overlapsBool')
        compareAttribute(self, aObj, bObj, n, transformDict, varNames, 'left-of')
        compareAttribute(self, aObj, bObj, n, transformDict, varNames, 'above')

        # Weighted Size transformation

        # if aObj.attributes['size'] != bObj.attributes['size']:
        compareAttribute(self, aObj, bObj, n, transformDict, varNames, 'size')

        # if 'size' in aObj.attributes and 'size' in bObj.attributes:
        #     transformDict[str(self, n) + varNames + 'SizeDiff'] = convertSize(self, aObj.attributes['size']) - convertSize(self, bObj.attributes['size'])
        #     print(str(n) + varNames + 'SizeDiff: ' + str(transformDict[str(n) + varNames + 'SizeDiff']))

        # make alignment transformation comparison
        if 'alignment' in aObj.attributes and 'alignment' in bObj.attributes:
            if aObj.attributes['alignment'] != bObj.attributes['alignment']:
                transformDict[str(n) + varNames + 'AlignDiff'] = aObj.attributes['alignment'] + '-' + bObj.attributes['alignment']
                # remove duplicate words
                transformDict[str(n) + varNames + 'AlignDiff'] = removeDuplicates(self, transformDict[str(n) + varNames + 'AlignDiff'])
                print(str(n) + varNames + 'AlignDiff: ' + transformDict[str(n) + varNames + 'AlignDiff'])

        # make fill transform:  if same int = 0, if different, int = 1
        # calculate AB fill difference
        if aObj.attributes['fill'] == bObj.attributes['fill']:
            transformDict[str(n) + varNames + 'FillDiff'] = 0
        elif aObj.attributes['fill'] == 'yes' and bObj.attributes['fill'] == 'no':
            transformDict[str(n) + varNames + 'FillDiff'] = -1  # if the fill changed across the transformation assign a 1
        elif aObj.attributes['fill'] == 'no' and bObj.attributes['fill'] == 'yes':
            transformDict[str(n) + varNames + 'FillDiff'] = 1  # if the fill changed

        # make transformation comparisons for angles:

        # print("making angle transformation comparisons")
        if 'angle' in aObj.attributes and 'angle' in bObj.attributes:  # check that this object has angles
            # calculate AB angle difference
            transformDict[str(n) + varNames + 'AngleDiff'] = int(aObj.attributes['angle']) - int(bObj.attributes['angle'])
            print(str(n) + varNames + " AngleDiff = " + str(transformDict[str(n) + varNames + 'AngleDiff']))

def compareObjtoAns(self, c, problem, x, varNames, varNames1, alignIncr, angleIncr, fillIncr, reflectIncr, shapeIncr, sizeIncr, overlapsIncr, overlapsBoolIncr, leftOfIncr, aboveIncr,
                    tot, transformDict, matchObjsDict):

    ansObjFigure = problem.figures[str(x)]
    # todo: choose min of the 2
    for n in range(len(matchObjsDict[str(c.name) + ', ' + str(x)])):
        cObjName, ansObjName = matchObjsDict[str(c.name) + ', ' + str(x)][n][0], matchObjsDict[str(c.name) + ', ' +str(x)][n][1]
        cObj, ansObj = c.objects[str(cObjName)], ansObjFigure.objects[ansObjName]

        # TODO: add new transforms comparing overlaps, left-of, and above.

        compareAttribute(self, cObj, ansObj, n, transformDict, varNames1, 'overlaps')
        compareAttribute(self, cObj, ansObj, n, transformDict, varNames1, 'overlapsBool')
        compareAttribute(self, cObj, ansObj, n, transformDict, varNames1, 'left-of')
        compareAttribute(self, cObj, ansObj, n, transformDict, varNames1, 'above')

        tot = calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, 'overlaps', overlapsIncr)
        tot = calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, 'overlapsBool', overlapsBoolIncr)

        tot = calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, 'left-of', leftOfIncr)
        tot = calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, 'above', aboveIncr)

        # make special case of square having properties of height and width and compare to rectangle
        convertSquareToRectangle(self, cObj)
        convertSquareToRectangle(self, ansObj)

         # compare to rectangle
        compHeightAndWidth(self, cObj, ansObj, n, transformDict, varNames1)

        tot = calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, 'height', sizeIncr)
        tot = calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, 'width', sizeIncr)

        # check for shape transform:
        # if cObj.attributes['shape'] != ansObj.attributes['shape']:

        transformDict[str(n) + varNames1 + 'ShapeDiff'] = (cObj.attributes['shape'] + '-' + ansObj.attributes['shape'])
        print('\nShape Transform for ' + str(n) + varNames1 + ': ' + transformDict[str(n) + varNames1 + 'ShapeDiff'])
        print('cObjName = ' + cObj.name + ' ansObjName = ' + ansObj.name)

        #if n == (len(matchObjsDict[str(c.name) + ', ' + str(x)]) - 1):
        if str(n) + varNames + 'ShapeDiff' in transformDict and str(n) + varNames1 + 'ShapeDiff' in transformDict:
            # the sorting corrects the issue of the same shapes appearing in different orders
            if (transformDict[str(n) + varNames + 'ShapeDiff']) == (transformDict[str(n) + varNames1 + 'ShapeDiff']):
                tot += shapeIncr
                print("CORRECT SHAPE TRANSFORM! FOR " + str(n) + varNames + varNames1)

        tot = calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, 'size', sizeIncr)

        # if 'size' in cObj.attributes and 'size' in ansObj.attributes:
        #     transformDict[str(n) + varNames1 + 'SizeDiff'] = convertSize(self, cObj.attributes['size']) - convertSize(self, ansObj.attributes['size'])
        #     print(str(n) + varNames1 + 'SizeDiff: ' + str(transformDict[str(n) + varNames1 + 'SizeDiff']))
        #     # if transformDict[str(n) + varNames + 'SizeDiff'] != '' and transformDict[str(n) + varNames1 + 'SizeDiff'] != '':
        #         # the sorting corrects the issue of the same sizes appearing in different orders
        # if str(n) + varNames + 'SizeDiff' in transformDict and str(n) + varNames1 + 'SizeDiff' in transformDict:
        #     if (transformDict[str(n) + varNames + 'SizeDiff']) == (transformDict[str(n) + varNames1 + 'SizeDiff']):
        #         tot += sizeIncr
        #         print("CORRECT SIZE TRANSFORM! FOR " + str(n) + varNames + varNames1)

        # calculate CD fill difference
        ansValue = ansObj.attributes['fill']
        if cObj.attributes['fill'] == ansValue:
            transformDict[str(n) + varNames1 + 'FillDiff'] = 0
        else:
            transformDict[str(n) + varNames1 + 'FillDiff'] = 1
            # Make fill transformation comparison:
        if str(n) + varNames + 'FillDiff' in transformDict and str(n) + varNames1 + 'FillDiff' in transformDict:
            if transformDict[str(n) + varNames + 'FillDiff'] == transformDict[str(n) + varNames1 + 'FillDiff']:
                tot += fillIncr
                print("CORRECT ab = cd FILL transformations!")

        # check alignment transform
        if 'alignment' in cObj.attributes and 'alignment' in ansObj.attributes:
            if cObj.attributes['alignment'] != ansObj.attributes['alignment']:
                transformDict[str(n) + varNames1 + 'AlignDiff'] = cObj.attributes['alignment'] + '-' + ansObj.attributes['alignment']
                print(str(n) + varNames1 + 'AlignDiff: ' + transformDict[str(n) + varNames1 + 'AlignDiff'])
                # remove duplicate words
                transformDict[str(n) + varNames1 + 'AlignDiff'] = removeDuplicates(self, transformDict[str(n) + varNames1 + 'AlignDiff'])
                print(str(n) + varNames1 + 'AlignDiff: ' + transformDict[str(n) + varNames1 + 'AlignDiff'])
        # calculate alignment transform differences
        # if sorted(transformDict[str(n) + varNames + 'AlignDiff']) == sorted(transformDict[str(n) + varNames1 + 'AlignDiff']) and transformDict[
        #     str(n) + varNames + 'AlignDiff'] != 'empty-' and transformDict[str(n) + varNames1 + 'AlignDiff'] != 'empty-':
            if (str(n) + varNames + 'AlignDiff') in transformDict and (str(n) + varNames1 + 'AlignDiff') in transformDict:
                if (transformDict[str(n) + varNames + 'AlignDiff']) == (transformDict[str(n) + varNames1 + 'AlignDiff']) and transformDict[
                    str(n) + varNames + 'AlignDiff'] != 'empty-' and transformDict[str(n) + varNames1 + 'AlignDiff'] != 'empty-':
                    tot += alignIncr
                    print("CORRECT Align transformations! for " + str(n) + varNames + varNames1)

        # if angle transformation equal tot+=1

        if 'angle' in cObj.attributes and 'angle' in ansObj.attributes:  # check that this object has angles
            transformDict[str(n) + varNames1 + 'AngleDiff'] = int(cObj.attributes['angle']) - int(ansObj.attributes['angle'])
            print("cdAngleDiff= " + str(transformDict[str(n) + varNames1 + 'AngleDiff']))

         # check for angle transformation
        # TODO: troubleshoot angle transformation comparisons
        if str(n) + varNames + 'AngleDiff' in transformDict and str(n) + varNames1 + 'AngleDiff' in transformDict:
            if abs(transformDict[str(n) + varNames + 'AngleDiff'] + 180) % 360 == abs(transformDict[str(n) + varNames1 + 'AngleDiff']):
                tot += reflectIncr
                print("Same reflections for " + str(n) + varNames + varNames1)
            elif transformDict[str(n) + varNames + 'AngleDiff'] == transformDict[str(n) + varNames1 + 'AngleDiff']:
                tot += angleIncr
                print("Same angle transformations for " + str(n) + varNames + varNames1)

    return tot

def compareAttribute(self, aObj, bObj, n, transformDict, varNames, attribute):
    'attributeName has the first letter capitalized of attribute'
    attributeName = attribute.title()
    if attribute == 'size' or attribute == 'width' or attribute == 'height':
        if attribute in aObj.attributes and attribute in bObj.attributes:
            transformDict[str(n) + varNames + attributeName + 'Diff'] = convertSize(self,  aObj.attributes[
                attribute]) - convertSize(self,  bObj.attributes[attribute])
            print(str(n) + varNames + attributeName + 'Diff: ' + str(transformDict[str(n) + varNames + attributeName + 'Diff']))
    else:
        if attribute in aObj.attributes and attribute in bObj.attributes:
            transformDict[str(n) + varNames + attributeName + 'Diff'] = ( aObj.attributes[
                attribute]) + ( bObj.attributes[attribute])
            print(str(n) + varNames + attributeName + 'Diff: ' + str(transformDict[str(n) + varNames + attributeName + 'Diff']))

def addOverlapsBoolean(self, figure):
    'adds a boolean of overlapsBool to each object'
    for aObjName in figure.objects:
        aObj = figure.objects[aObjName]
        if 'overlaps' not in aObj.attributes:
            aObj.attributes['overlapsBool'] = 'no'
        else:
            aObj.attributes['overlapsBool'] = 'yes'

def convertOppositeAttributes(self, figure, attribute):
    ' add opposite attributes to the corresponding object which is left-of or above'
    if attribute == 'left-of':
        oppositeAttribute = 'right-of'
    elif attribute == 'above':
        oppositeAttribute = 'below'
    elif attribute == 'inside':
        oppositeAttribute = 'outside'

    for aObjName in figure.objects:
        aObj = figure.objects[aObjName]
        if attribute in aObj.attributes:
            for bObjName in aObj.attributes[attribute].split(','):
                bObj = figure.objects[bObjName]
                if oppositeAttribute in bObj.attributes:
                    bObj.attributes[oppositeAttribute] += aObjName
                else:
                    bObj.attributes[oppositeAttribute] = aObjName

def compareOppositeAttributes(self, aObj, bObj, n, transformDict, varNames, attribute):
    attributeName = attribute.title()
    if attribute == 'left-of':
        oppositeAttribute = 'right-of'
    elif attribute == 'above':
        oppositeAttribute = 'below'
    elif attribute == 'inside':
        oppositeAttribute = 'outside'

    if attribute in aObj.attributes and oppositeAttribute in bObj.attributes :
        # add attribute1 to corresponding b object
        transformDict[str(n) + varNames + attributeName + 'Diff'] = (aObj.attributes[
            attribute]) + ' ' + (bObj.attributes[oppositeAttribute])
        print(str(n) + varNames + attributeName + 'Diff: ' + str(transformDict[str(n) + varNames + attributeName + 'Diff']))

def calculateOppositeTransformEquality(self, n, tot, transformDict, varNames, varNames1, attribute, attrIncr):
    attributeName = attribute.title()
    if attribute == 'left-of':
        oppositeAttribute = 'right-of'
    elif attribute == 'above':
        oppositeAttribute = 'below'
    elif attribute == 'inside':
        oppositeAttribute = 'outside'
    oppositeAttributeName = oppositeAttribute.title()

    if str(n) + varNames + attributeName + 'Diff' in transformDict and str(n) + varNames1 + attributeName + 'Diff' in transformDict:
        if (transformDict[str(n) + varNames + attributeName + 'Diff']) == (transformDict[str(n) + varNames1 + attributeName + 'Diff']):
            tot += attrIncr
            print("CORRECT " + attributeName + " TRANSFORM FOR " + str(n) + varNames + varNames1)
    return tot

def compHeightAndWidth(self, aObj, bObj, n, transformDict, varNames):
    if 'height' in aObj.attributes and 'height' in bObj.attributes:
        transformDict[str(n) + varNames + 'HeightDiff'] = convertSize(self, aObj.attributes[
            'height']) - convertSize(self, bObj.attributes['height'])
        print(str(n) + varNames + 'HeightDiff: ' + str(transformDict[str(n) + varNames + 'HeightDiff']))
    if 'width' in aObj.attributes and 'width' in bObj.attributes:
        transformDict[str(n) + varNames + 'WidthDiff'] = convertSize(self, aObj.attributes[
            'width']) - convertSize(self, bObj.attributes['width'])
        print(str(n) + varNames + 'WidthDiff: ' + str(transformDict[str(n) + varNames + 'WidthDiff']))

def calculateTransformEquality(self, n, tot, transformDict, varNames, varNames1, attribute, attrIncr):
    attributeName = attribute.title()
    if str(n) + varNames + attributeName + 'Diff' in transformDict and str(n) + varNames1 + attributeName + 'Diff' in transformDict:
        if (transformDict[str(n) + varNames + attributeName + 'Diff']) == (transformDict[str(n) + varNames1 + attributeName + 'Diff']):
            tot += attrIncr
            print("CORRECT " + attributeName + " TRANSFORM FOR " + str(n) + varNames + varNames1)
    return tot

def convertSquareToRectangle(self, aObj):
    if aObj.attributes['shape'] == 'square' and 'height' not in aObj.attributes and 'width' not in aObj.attributes:
        aObj.attributes['height'] = aObj.attributes['size']
        aObj.attributes['width'] = aObj.attributes['size']

def convertSize(self, size):
    ' converts object size to integer'
    if size == 'very small':
        return 1
    elif size == 'small':
        return 2
    elif size == 'medium':
        return 3
    elif size == 'large':
        return 4
    elif size == 'very large':
        return 5
    elif size == 'huge':
        return 6

def removeDuplicates(self, inputString):
    alignList = ''
    alignList = inputString.split('-')
    listString = ''
    removeWords = []
    for word in alignList:
        if word in listString:
            removeWords.append(word)
        else:
            listString += word
    for removeWord in removeWords:
        listString = listString.replace(removeWord, "")
    return listString

def sortDict(dict):
    # return sorted(dict, key=dict.get)
    return dict