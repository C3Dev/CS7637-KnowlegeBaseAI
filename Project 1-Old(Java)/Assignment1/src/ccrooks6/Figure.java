package ccrooks6;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import ravensproject.RavensFigure;
import ravensproject.RavensObject;
import ravensproject.RavensProblem;

/*This class will hold as the basis for all the figures
 * Each figure is labeled A,B,C,D and 1,2,3,4,5,6
 * The figures are the superclass of the Object.
 *
 * The hierarchy model is as follows:
 * 	RavensProblem -> has Figures -> has objects
 *
 */
public class Figure {

	// ultimately they will be static and never changing.
	String figureName;
	RavensObject ro;
	HashMap<String, RavensObject> objects;
	Object o;
	HashMap<String, RavensFigure> figureList;
	public String problemName;
	// Attribute a,b;
	ArrayList a, b, c, one, two, three, four, five, six, similarites;
	ArrayList abSimilarties, abDifferences; 
	List<ArrayList> absim ;
	List<ArrayList> abdiff;

	ArrayList cFigSimilarties, cFigDifferences; 
	List<ArrayList> cFigsim;
	List<ArrayList> cFigdiff;

	
	
	String answer;
	
	public int weight;
	/*
	 * No Transformation = 10 Fill Transformation = 9 Angle, verticle-flip trans
	 * = 8 Size transformation = 7 Spatial transformation (in this order inside,
	 * left-of and above) = 5 Shape transformation = 3 Unknown transformation =
	 * 0
	 */
	boolean isObject;
	int totalAAttributes;

	public Figure() {

		a = new ArrayList();
		b = new ArrayList();
		c = new ArrayList();
		one = new ArrayList();
		two = new ArrayList();
		three = new ArrayList();
		four = new ArrayList();
		five = new ArrayList();
		six = new ArrayList();


	}


	public void generateTest() throws IOException
	{
		ArrayList<Attribute> listC = new ArrayList<Attribute>(); 
		for(int f = 1; f <= 6; f++){
		ArrayList numObject = new ArrayList(); 	
		String number = " ";
		switch(f)
		{
		case 1 : number = "1"; numObject = one; 
		break;
		case 2 : number = "2";numObject = two; 
		break;
		case 3 : number = "3";numObject = three; 
		break;
		case 4 : number = "4";numObject = four; 
		break;
		case 5 : number = "5";numObject = five; 
		break;
		case 6 : number = "6";numObject = six; 
		break;}
		
		final int totalC = o.getObjectCount("C");
		final int totalNumber= o.getObjectCount(number);
		
	
		String[] split = new String[600];
		String shapeA = " ";
		String object = "";
		String size = "";
		Attribute figA = null;
		Attribute figB = null;
	
		ArrayList<Attribute> listone = new ArrayList<Attribute>(); 
		Object objC = new Object();
		Object objone = new Object();
		// this counts the objects 
		
		String historyObject = "";
		// by this if it reduces time complexity. of n^2 
		// this will generate C's values. 
		if(f == 1){
	for(int j = 0; j < totalC; j++){
		
		
		// needed 
		objC.printObjectValues("C");
		objC.getObjectValues();  // returns A and b 
		objone.printObjectValues(number);
		objone.getObjectValues(); // returns C and D 
	
		
	
		
		for (int i = 0; i < c.size(); i++) {
			split = numObject.get(i).toString().split(" ");
			String test = split[0];
	
			if(!historyObject.equals(historyObject) || historyObject.equals("") || !test.equals(historyObject)){
				listC.add(figA);
				figA  = new Attribute(); 
			}
					
			historyObject = split[0]; 
	
			
			if (c.get(i).toString().contains("shape")) {
				shapeA = split[2];
				figA.hasShape = true;
				figA.shape = split[2];
			}
			if (c.get(i).toString().contains("size")) {
				if(split[2].equals("very"))
					figA.size = split[2] + " " +split[3];
					else{
						figA.size = split[2]; 
					}
				figA.hasSize = true;
				
			}

	if (c.get(i).toString().contains("fill")) {
				
				figA.hasfill = true;
				figA.fill = split[2];
			}
		  
	
	if (c.get(i).toString().contains("angle")) {
		
		figA.hasAngle = true;
		figA.angle = split[2];
	}
  
	if (c.get(i).toString().contains("inside")) {
		
		figA.hasInside = true;
		figA.inside = split[2];
	}
	
	
	
		}
		listC.add(figA);
	
	}// end first for 
		}
	
	
	for(int j = 0; j < totalC; j++){

			
		for (int i = 0; i < numObject.size(); i++) {


			split = b.get(i).toString().split(" ");
			String test = split[0];
	
			if(!historyObject.equals(historyObject) || historyObject.equals("") || !test.equals(historyObject)){
				listone.add(figB);
				figB  = new Attribute(); 
			}
					
			historyObject = split[0]; 
			
	
			
			if (numObject.get(i).toString().contains("shape")) {
				
				figB.hasShape = true;
				figB.shape = split[2];
			}
			if (numObject.get(i).toString().contains("size")) {
				
				if(split[2].equals("very"))
					figB.size = split[2] + " " +split[3];
					else{
						figB.size = split[2]; 
					}
				figB.hasSize = true;
				figB.size = size;
			}

	if (numObject.get(i).toString().contains("fill")) {
				
				figB.hasfill = true;
				figB.fill = split[2];
			}
		  
		
		
		if (numObject.get(i).toString().contains("angle")) {
			
			figB.hasAngle = true;
			figB.angle = split[2];
		}
	  
		if (numObject.get(i).toString().contains("inside")) {
			
			figB.hasInside = true;
			figB.inside = split[2];
		}
		
		}
		listone.add(figB);
	
	}// end first for 
	
	

	getSimiliartiesAB(listC, listone, f,2); 

		
		} // end first for loop. 

	}
	
	
	
	
	// needs to have the same values.
	public void setSimilarites() throws IOException {
		System.out.println("THE SIZE OF A is " +a.size());
		
		// drill down the attributes.
		similarites = new ArrayList();
		final int totalA = o.getObjectCount("A");
		final int totalB = o.getObjectCount("B");
		if (totalA != totalB) {
			System.out.println("A or B has more objects than the other");
		}
		else {System.out.println("Figures have same amount of Objects");}

		String[] split = new String[600];
		String shapeA = " ";
		String object = "";
		String size = "";
		Attribute figA = null;
		Attribute figB = null;
		ArrayList<Attribute> listA = new ArrayList<Attribute>(); 
		ArrayList<Attribute> listB = new ArrayList<Attribute>(); 
		Object objA = new Object();
		Object objB = new Object();
		// this counts the objects 
		String historyObject = "";  
		
	
		// this needs to make a new arraylist for each group of objects 
	
		
		// needed 
		objA.printObjectValues("A");
		objA.getObjectValues();  // returns A and b 
		objB.printObjectValues("B");
		objB.getObjectValues(); // returns C and D 
	
		System.out.println("TEST A "  + a);
		System.out.println("TEST B "  + b);
		// all good up to here. 
			

		
		for (int i = 0; i < a.size(); i++) {
			
			split = a.get(i).toString().split(" ");
			String test = split[0];
	
			if(!historyObject.equals(historyObject) || historyObject.equals("") || !test.equals(historyObject)){
				listA.add(figA);
				figA  = new Attribute(); 
			}
					
			historyObject = split[0]; 
			
			if (a.get(i).toString().contains("shape")) {
				shapeA = split[2];
				figA.hasShape = true;
				figA.shape = split[2];
			}
			if (a.get(i).toString().contains("size")) {
				if(split[2].equals("very"))
				size = split[2] + " " +split[3];
				else{
					size = split[2]; 
				}
				figA.hasSize = true;
				figA.size = size;
			}

	if (a.get(i).toString().contains("fill")) {
				
				figA.hasfill = true;
				figA.fill = split[2];
			}
	
	if (a.get(i).toString().contains("angle")) {
		
		figA.hasAngle = true;
		figA.angle = split[2];
	}
  
	if (a.get(i).toString().contains("inside")) {
		
		figA.hasInside = true;
		figA.inside = split[2];
	}
  
	
}
		listA.add(figA);
	
// error
	
	for(int j = 0; j < totalB; j++){
		
		
		for (int i = 0; i < b.size(); i++) {
	
			split = b.get(i).toString().split(" ");
			String test = split[0];
	
			if(!historyObject.equals(historyObject) || historyObject.equals("") || !test.equals(historyObject)){
				listB.add(figB);
				figB  = new Attribute(); 
			}
					
			historyObject = split[0]; 
			
			if (b.get(i).toString().contains("shape")) {
				
				figB.hasShape = true;
				figB.shape = split[2];
			}
			if (b.get(i).toString().contains("size")) {
				
				if(split[2].equals("very"))
					size = split[2] + " " +split[3];
					else{
						size = split[2]; 
					}
					figB.hasSize = true;
					figB.size = size;
			}

	if (b.get(i).toString().contains("fill")) {
				
				figB.hasfill = true;
				figB.fill = split[2];
			}
	
	
if (b.get(i).toString().contains("angle")) {
		
		figB.hasAngle = true;
		figB.angle = split[2];
	}
  
	if (b.get(i).toString().contains("inside")) {
		
		figB.hasInside = true;
		figB.inside = split[2];
	}
		  
		}
		listB.add(figB);
	
	}// end first for 
	
	
	
	
	getSimiliartiesAB(listA, listB,0, 1); 

	}

	// BIG METHOD BIG IMPLEMENTATION 
	public void getSimiliartiesAB(ArrayList<Attribute> listA, ArrayList<Attribute> listB, int setting, int procedure)
	{
		// 0 holds object 1 
		// 1 holds object 2 
		
		// check what values are there.
		
		// Step 1 make sure that the lists have the same amount of objects
		ArrayList similarites = null; 
		ArrayList differences = null; 
		List<ArrayList> sim = new ArrayList(); 
		List<ArrayList> diff = new ArrayList(); 
		if(listA.size() == listB.size())
		{
			// objects have the same size. 
			for(int i = 1; i < listA.size(); i++)
			{
				boolean aSize = listA.get(i).hasSize;
				boolean aShape = listA.get(i).hasShape;
				boolean aFill = listA.get(i).hasfill; 
				boolean aAngle = listA.get(i).hasAngle;
				boolean aInside= listA.get(i).hasInside; 
				
				boolean bSize = listB.get(i).hasSize;
				boolean bShape = listB.get(i).hasShape;
				boolean bFill = listB.get(i).hasfill; 
				boolean bAngle = listB.get(i).hasAngle;
				boolean bInside= listB.get(i).hasInside; 
				
			//-------------------------------------------------------- 	
				String aSizeVal =  listA.get(i).size;
				String aShapeVal =  listA.get(i).shape;
				String afillVal=  listA.get(i).fill;
				String aAngleVal =  listA.get(i).angle;
				String aInsideVal=  listA.get(i).inside;
				// ------------------------------------------
				// B figure
				String bSizeVal =  listB.get(i).size;
				String bShapeVal =  listB.get(i).shape;
				String bfillVal=  listB.get(i).fill;
				String bAngleVal =  listB.get(i).angle;
				String bInsideVal=  listB.get(i).inside;
				
				similarites = new ArrayList();

				differences = new ArrayList();
				
				if(aSize && bSize)
				{
					if(aSizeVal.equals(bSizeVal)){
						similarites.add("size " + aSizeVal);
					}else{
						// they are different. 
						differences.add("size " + bSizeVal); // the one it changes to. 
					}
				}
				
				if(aShape && bShape)
				{
					if(aShapeVal.equals(bShapeVal)){
						similarites.add("shape " + aShapeVal);
					}else{
						// they are different. 
						differences.add("shape " + bShapeVal); // the one it changes to. 
					}
				}
				
				
				if(aFill && bFill)
				{
					if(afillVal.equals(bfillVal)){
						similarites.add("fill " + afillVal);
					}else{
						// they are different. 
						differences.add("fill " + bfillVal); // the one it changes to. 
					}
				}
				if(aAngle && bAngle)
				{
					if(aAngleVal.equals(bAngleVal)){
						similarites.add("angle " + aAngleVal);
					}else{
						// they are different. 
						differences.add("angle " + bAngleVal); // the one it changes to. 
					}
				}
				
				
				if(aInside && bInside)
				{
					if(aInsideVal.equals(bInsideVal)){
						similarites.add("inside " + aInsideVal);
					}else{
						// they are different. 
						differences.add("inside " + bInsideVal); // the one it changes to. 
					}
				}
				
				
				
				sim.add(similarites);
				diff.add(differences);
				// dont know how to handle this yet 
				if(procedure == 1){
				abSimilarties = similarites; 
				abDifferences = differences; 
				
				absim = sim;
				abdiff = diff; 
				}
				else if (procedure == 2)
				{
					cFigSimilarties = similarites; 
					cFigDifferences = differences;
					cFigsim = sim;
					cFigdiff = diff; 
				}
			
				
				// now i have the sim and differences in a list. 
				
			}
			
			
		}
		
		
		
		
		if(setting == 0){
		
		System.out.println("THE SIMILARITES of A and B  : " + abSimilarties);

		System.out.println("THE differences of A and B : " + abDifferences);
		}
		if(setting == 1)
		{	System.out.println("THE SIMILARITES of C and 1: " + abSimilarties);

		System.out.println("THE differences of C and 1 : " + abDifferences);
			
		}
		if(setting == 2)
		{	System.out.println("THE SIMILARITES of C and 2: " + abSimilarties);

		System.out.println("THE differences of C and 2 : " + abDifferences);
			
		}
		if(setting == 3)
		{	System.out.println("THE SIMILARITES of C and 3: " + abSimilarties);

		System.out.println("THE differences of C and 3 : " + abDifferences);
			
		}
		if(setting == 4)
		{	System.out.println("THE SIMILARITES of C and 4: " + abSimilarties);

		System.out.println("THE differences of C and 4 : " + abDifferences);
			
		}
		
		if(setting == 5)
		{	System.out.println("THE SIMILARITES of C and 5: " + abSimilarties);

		System.out.println("THE differences of C and 5 : " + abDifferences);
			
		}
		if(setting == 6)
		{	System.out.println("THE SIMILARITES of C and 6: " + abSimilarties);

		System.out.println("THE differences of C and 6 : " + abDifferences);
			
		}
		
		
		
		
		if(differences.size() == 0)
		{
			System.out.println("The Answer is " + setting);
		}
		
		
		
	}
	
	
	
	
	
	public void printA() {
		for (int i = 0; i < a.size(); i++) {
			System.out.println(a.get(i));
		}
	}

	public void printB() {
		for (int i = 0; i < b.size(); i++) {
			System.out.println(b.get(i));
		}
	}

	public void printone() {
		for (int i = 0; i < one.size(); i++) {
			System.out.println(one.get(i));
		}
	}

	public void printtwo() {
		for (int i = 0; i < two.size(); i++) {
			System.out.println(two.get(i));
		}
	}

	public void setProblem(final String problem) {
		problemName = problem;
	}

	// first lets set the map of figures.

	public void setFigureList(final HashMap<String, RavensFigure> figureList) {
		this.figureList = figureList;
	}

	public void setAttributes(final RavensProblem problem) {
	
		for(String figureName : problem.getFigures().keySet()) {
			RavensFigure thisFigure = problem.getFigures().get(figureName);
				
			
		// note this is n^2
		for (final String objectName : thisFigure.getObjects().keySet()) {
			final RavensObject thisObject = thisFigure.getObjects().get(
					objectName);
			for (final String attributeName : thisObject.getAttributes()
					.keySet()) {
				final String attributeValue = thisObject.getAttributes().get(
						attributeName);
				 System.out.println(figureName + " " + objectName + " "
				 + attributeName + " " + attributeValue);

				if (figureName.contains("A")) {
					a.add(thisObject.getName() + " " + attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("B")) {
					b.add(thisObject.getName()  + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("C")) {
					c.add(thisObject.getName()  + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("1")) {
					one.add(thisObject.getName() + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("2")) {
					two.add(thisObject.getName() + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("3")) {
					three.add(thisObject.getName()  + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("4")) {
					four.add(thisObject.getName()  + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("5")) {
					five.add(thisObject.getName()  + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("6")) {
					six.add(thisObject.getName()  + " " +attributeName + " "
							+ attributeValue);
				}
			}
			}

		}
		
	}

	public void setObjects(final HashMap<String, RavensObject> objects)
			throws IOException { // iterate over and set objects based on
		// figure.

		this.objects = objects;

		// once objects are set pass it to the Object variable
		o = new Object(objects);

		printObjects();

		//o.printObjectValues(figureName); // this will count the values in
		// figure.

		// now i got each figure object from each figure.
		// now need to set attributes and solve this thing

	}

	public void printObjects() throws IOException {

		o.printFigureObjects(figureName);
	}

	public void getTotalObjects() {

	}

	public String getFigureName() {
		return figureName;
	}

	public void setFigureName(final String figureName) {
		this.figureName = figureName;
	}

}
