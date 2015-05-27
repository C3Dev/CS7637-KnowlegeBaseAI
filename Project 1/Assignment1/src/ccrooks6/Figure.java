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

	}


	
	
	
	
	
	// needs to have the same values.
	public void setSimilarites() throws IOException {

		// drill down the attributes.
		similarites = new ArrayList();
		final int totalA = o.getObjectCount("A");
		final int totalB = o.getObjectCount("B");
		if (totalA != totalB) {
			System.out.println("A or B has more objects than the other");
		}
		System.out.println("Figures have same amount of Objects");

		String[] split = new String[600];
		String shapeA = " ";
		String object = "";
		String size = "";
		Attribute figA = new Attribute(); 
		
		// this counts the objects 
	for(int j = 0; j < totalA; j++){
		Attribute a1 = new Attribute(); // create a new object everytime. 
		for (int i = 0; i < a.size(); i++) {
		
			
			
			split = a.get(i).toString().split(" ");
			object = split[0];
			a1.ObjectName = object; 
			
			if (a.get(i).toString().contains("shape")) {
				shapeA = split[2];
				figA.hasShape = true;
				figA.shape = split[2];
			}
			if (a.get(i).toString().contains("size")) {
				shapeA = split[2];
				figA.hasShape = true;
				figA.shape = split[2];
			}

		}
		
	}// end first for 

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
		final RavensFigure thisFigure = problem.getFigures().get(figureName);

		a = new ArrayList();
		b = new ArrayList();
		c = new ArrayList();
		one = new ArrayList();
		two = new ArrayList();
		three = new ArrayList();
		four = new ArrayList();
		five = new ArrayList();
		six = new ArrayList();

		// note this is n^2
		for (final String objectName : thisFigure.getObjects().keySet()) {
			final RavensObject thisObject = thisFigure.getObjects().get(
					objectName);
			for (final String attributeName : thisObject.getAttributes()
					.keySet()) {
				final String attributeValue = thisObject.getAttributes().get(
						attributeName);
				// System.out.println(figureName + " " + objectName + " "
				// + attributeName + " " + attributeValue);

				if (figureName.contains("A")) {
					a.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("B")) {
					b.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("C")) {
					c.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("1")) {
					one.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("2")) {
					two.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("3")) {
					three.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("4")) {
					four.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("5")) {
					five.add(attributeName + " "
							+ attributeValue);
				}
				if (figureName.contains("6")) {
					six.add(attributeName + " "
							+ attributeValue);
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

		o.printObjectValues(figureName); // this will count the values in
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
