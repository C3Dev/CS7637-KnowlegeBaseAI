package ccrooks6;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

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
		
		final int totalC = o.getObjectCount("C");
		final int totalone = o.getObjectCount("1");
		
		
		if (totalC != totalone) {
			
		}
		else {}

		String[] split = new String[600];
		String shapeA = " ";
		String object = "";
		String size = "";
		Attribute figA;
		Attribute figB;
		ArrayList<Attribute> listC = new ArrayList<Attribute>(); 
		ArrayList<Attribute> listone = new ArrayList<Attribute>(); 
		Object objC = new Object();
		Object objone = new Object();
		// this counts the objects 
		
		
	for(int j = 0; j < totalC; j++){
		// this needs to make a new arraylist for each group of objects 
		figA  = new Attribute(); 
		
		// needed 
		objC.printObjectValues("C");
		objC.getObjectValues();  // returns A and b 
		objone.printObjectValues("1");
		objone.getObjectValues(); // returns C and D 
	
		
		ArrayList att;
		
		for (int i = 0; i < c.size(); i++) {
		att = new ArrayList();
			split = a.get(i).toString().split(" ");
	
			
			if (c.get(i).toString().contains("shape")) {
				shapeA = split[2];
				figA.hasShape = true;
				figA.shape = split[2];
			}
			if (c.get(i).toString().contains("size")) {
				size = split[2] + " " +split[3];
				figA.hasSize = true;
				figA.size = size;
			}

	if (c.get(i).toString().contains("fill")) {
				
				figA.hasFill = true;
				figA.fill = split[2];
			}
		  
		}
		listC.add(figA);
	
	}// end first for 
	
	
	
	for(int j = 0; j < totalC; j++){
		// this needs to make a new arraylist for each group of objects 
		figB  = new Attribute(); 
		
			
		ArrayList att;
		
		for (int i = 0; i < b.size(); i++) {
		att = new ArrayList();
			split = one.get(i).toString().split(" ");
	
			
			if (one.get(i).toString().contains("shape")) {
				
				figB.hasShape = true;
				figB.shape = split[2];
			}
			if (one.get(i).toString().contains("size")) {
				
				figB.hasSize = true;
				figB.size = split[2] + " " +split[3];
			}

	if (one.get(i).toString().contains("fill")) {
				
				figB.hasFill = true;
				figB.fill = split[2];
			}
		  
		}
		listone.add(figB);
	
	}// end first for 
	
	

	getSimiliartiesAB(listC, listone, 2); 

		
		

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
		Attribute figA;
		Attribute figB;
		ArrayList<Attribute> listA = new ArrayList<Attribute>(); 
		ArrayList<Attribute> listB = new ArrayList<Attribute>(); 
		Object objA = new Object();
		Object objB = new Object();
		// this counts the objects 
		
		
	for(int j = 0; j < totalA; j++){
		// this needs to make a new arraylist for each group of objects 
		figA  = new Attribute(); 
		
		// needed 
		objA.printObjectValues("A");
		objA.getObjectValues();  // returns A and b 
		objB.printObjectValues("B");
		objB.getObjectValues(); // returns C and D 
	
		System.out.println("TEST A "  + a);
		System.out.println("TEST B "  + b);
		// all good up to here. 
			
		ArrayList att;
		
		for (int i = 0; i < a.size(); i++) {
		att = new ArrayList();
			split = a.get(i).toString().split(" ");
	
			
			if (a.get(i).toString().contains("shape")) {
				shapeA = split[2];
				figA.hasShape = true;
				figA.shape = split[2];
			}
			if (a.get(i).toString().contains("size")) {
				size = split[2] + " " +split[3];
				figA.hasSize = true;
				figA.size = size;
			}

	if (a.get(i).toString().contains("fill")) {
				
				figA.hasFill = true;
				figA.fill = split[2];
			}
		  
		}
		listA.add(figA);
	
	}// end first for 
	
	
	
	for(int j = 0; j < totalB; j++){
		// this needs to make a new arraylist for each group of objects 
		figB  = new Attribute(); 
		
			
		ArrayList att;
		
		for (int i = 0; i < b.size(); i++) {
		att = new ArrayList();
			split = a.get(i).toString().split(" ");
	
			
			if (b.get(i).toString().contains("shape")) {
				
				figB.hasShape = true;
				figB.shape = split[2];
			}
			if (b.get(i).toString().contains("size")) {
				
				figB.hasSize = true;
				figB.size = split[2] + " " +split[3];
			}

	if (b.get(i).toString().contains("fill")) {
				
				figB.hasFill = true;
				figB.fill = split[2];
			}
		  
		}
		listB.add(figB);
	
	}// end first for 
	
	
	
	
	getSimiliartiesAB(listA, listB,1); 

	}

	// BIG METHOD BIG IMPLEMENTATION 
	public void getSimiliartiesAB(ArrayList<Attribute> listA, ArrayList<Attribute> listB, int setting)
	{
		// check what values are there.
		boolean aSize = listA.get(0).hasSize;
		boolean aShape = listA.get(0).hasShape;
		boolean aFill = listA.get(0).hasFill; 
		
		boolean bSize = listB.get(0).hasSize;
		boolean bShape = listB.get(0).hasShape;
		boolean bFill = listB.get(0).hasFill; 
	//-------------------------------------------------------- 	
		String aSizeVal =  listA.get(0).size;
		String aShapeVal =  listA.get(0).shape;
		String afillVal=  listA.get(0).fill;
		// ------------------------------------------
		// B figure
		String bSizeVal =  listB.get(0).size;
		String bShapeVal =  listB.get(0).shape;
		String bfillVal=  listB.get(0).fill;
		
		
		ArrayList similarites = new ArrayList();

		ArrayList differences = new ArrayList();
		
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
		
		
		
		abSimilarties = similarites; 
		abDifferences = differences; 
		
		if(setting == 1){
		
		System.out.println("THE SIMILARITES ARE : " + abSimilarties);

		System.out.println("THE differences ARE : " + abDifferences);
		}
		if(setting == 2)
		{	System.out.println("THE SIMILARITES of C and 1: " + abSimilarties);

		System.out.println("THE differences of C and 1 : " + abDifferences);
			
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
					one.add(figureName + " " +attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("2")) {
					two.add(figureName + " " +attributeName + " "
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
