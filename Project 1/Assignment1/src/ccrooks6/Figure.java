package ccrooks6;

import java.util.HashMap;

import ravensproject.RavensObject;

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
	public Figure()
	{
	
	}

	public void setObjects(HashMap<String, RavensObject> objects)
	{ // iterate over and set objects based on figure. 

		this.objects = objects;
	}
	
	public void getTotalObjects()
	{
		
	}
	
	public void printObjectValues()
	{
		for (RavensObject ro : objects.values()) {
			
			System.out.println("Printing Objects for figure " + figureName); 
			System.out.println(ro.getName());
		}
		
	}

		
	
	public String getFigureName()
	{
		return figureName;
	}
	
	public void setFigureName(String figureName)
	{
		this.figureName = figureName; 
	}

	
	
}
