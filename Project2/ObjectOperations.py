class Operations:
	matchObjsDict = {} # dictionary to match objects
	attributeList = {'size':10, 'shape':15,'fill':5, 'angle':5, 'alignment':4,'above':4,'inside':4, 'left-of':4}
	matchObjsList = []
	
	def __init__(self):
		pass

	def matchObjects(self, fig1, fig2, matchObjsDict):
		#attributeList,incrList  need to be handled. 
		
		candidateObjsList = [] # candidate object of fig2 list, will be removed once matched
		
		self.CheckMissingObjects(fig1.objects, fig2.objects,candidateObjsList)
		self.CheckMissingObjects(fig2.objects, fig1.objects,candidateObjsList)
		matchObjsDict[str(fig1.name) + ', ' +str(fig2.name)] = self.matchObjsList
		return matchObjsDict
		
	def CheckMissingObjects(self, fig1objects, fig2objects, candidateObjsList):
		attributeList2 = list(self.attributeList.keys())
		incrList  = list(self.attributeList.values())
		#check to see if fig2 has more objects than fig1 
		if len(fig2objects) >= len(fig1objects):
			#put all the items in list from second object and delete from first to check missing
			for obj2name in sorted(fig2objects):
				candidateObjsList.append(fig2objects[obj2name])
			for obj1Name in sorted(fig1objects):
				obj1 = fig1objects[obj1Name]
				maxObj = None
				maxTot = 0 
				for obj2 in candidateObjsList:
					tot = 0
					for n in range(len(attributeList2)):
						attributeName = attributeList2[n]
						incr = incrList[n]

						if attributeName in obj1.attributes and attributeName in obj2.attributes:
							if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
								tot += incr
						if n < len(attributeList2)-1:
							attributeName1 = attributeList2[n+1]
							incr1 = incrList[n+1]
							if attributeName in obj1.attributes and attributeName in obj2.attributes and attributeName1 in obj1.attributes and attributeName1 in obj2.attributes:
								if obj2.attributes[attributeName] == obj1.attributes[attributeName] and obj2.attributes[attributeName1] == obj1.attributes[attributeName1]:
									tot += (incr + incr1) * 10
					if tot > maxTot:
						maxTot = tot
						maxObj = obj2
				if maxObj is not None:
					self.matchObjsList.append((obj1.name, maxObj.name))
					candidateObjsList.remove(maxObj)


			