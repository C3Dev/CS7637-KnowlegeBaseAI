package ccrooks6;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.HashMap;

import ravensproject.RavensObject;

public class Object extends Figure {

	public int count;
	public String figureBackup;
	HashMap<String, String> list;

	HashMap<String, RavensObject> objects;

	public Object() {

		count = 0;
		list = new HashMap<String, String>();
	}

	public Object(final HashMap<String, RavensObject> objects) {
		this.objects = objects;
	}

	public void setNumObjects(final int count) {
		this.count = count;
	}

	public void printFigureObjects(final String figureName) throws IOException {
		FileOutputStream outputStream;
		OutputStreamWriter outputStreamWriter;
		BufferedWriter bufferedWriter = null;
		outputStream = new FileOutputStream("Figure" + figureName + ".txt");
		outputStreamWriter = new OutputStreamWriter(outputStream, "UTF-16");
		bufferedWriter = new BufferedWriter(outputStreamWriter);

		// start up the file
		bufferedWriter
				.write("This file is used to store details about each figure \n");

		bufferedWriter.write("Objects in the Figure: ");
		bufferedWriter.newLine();
		bufferedWriter
				.write("-----------------------------------------------------");

		bufferedWriter.newLine();

		for (final RavensObject ro : objects.values()) {

			// System.out.println("Printing Objects for figure " + figureName);
			// System.out.println(ro.getName());

			// System.out.println(figureName + " " + pair.getKey());

			try {

				bufferedWriter.write("* " + " " + ro.getName());
				bufferedWriter.newLine();

			} catch (final IOException e) {
				e.printStackTrace();
			}

		}
		bufferedWriter
				.write("-----------------------------------------------------");
		bufferedWriter.close();
	}

	public void printObjectValues(final String figure) throws IOException {
		final String fileName = "Figure" + figure + ".txt";
	/*
		 * 
		 * 
		 * InputStream is = new BufferedInputStream(new
		 * FileInputStream(fileName)); // this will read the new file created
		 * use figure to open the file. try { byte[] c = new byte[1024]; int
		 * count = 0; int readChars = 0; boolean empty = true; while ((readChars
		 * = is.read(c)) != -1) { empty = false; for (int i = 0; i < readChars;
		 * ++i) {
		 * 
		 * if (c[i] == '\n') { ++count; } } } counter = (count == 0 && !empty) ?
		 * 1 : count; } finally { is.close(); }
		 * 
		 * 
		 * 
		 * System.out.println("The total objects in " + figure + " = " +
		 * counter); // this may be removed // could be set in the file analyzer
		 */
		int counter = 0; // this contains how many
		try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
			String line;
			while ((line = br.readLine()) != null) {
				if (line.contains("*")) {
					counter++;
				}
			}
			br.close();
		}

		System.out.println("The total objects in " + figure + " = " + counter); // this
																				// may
																				// be
																				// removed

	}

	public int getObjectCount(final String figure) throws IOException {
		final String fileName = "Figure" + figure + ".txt";
	/*
		 * 
		 * 
		 * InputStream is = new BufferedInputStream(new
		 * FileInputStream(fileName)); // this will read the new file created
		 * use figure to open the file. try { byte[] c = new byte[1024]; int
		 * count = 0; int readChars = 0; boolean empty = true; while ((readChars
		 * = is.read(c)) != -1) { empty = false; for (int i = 0; i < readChars;
		 * ++i) {
		 * 
		 * if (c[i] == '\n') { ++count; } } } counter = (count == 0 && !empty) ?
		 * 1 : count; } finally { is.close(); }
		 * 
		 * 
		 * 
		 * System.out.println("The total objects in " + figure + " = " +
		 * counter); // this may be removed // could be set in the file analyzer
		 */
		int counter = 0; // this contains how many
		try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
			String line;
			while ((line = br.readLine()) != null) {
				if (line.contains("*")) {
					counter++;
				}
			}
			br.close();
		}

		return counter;

	}
}
