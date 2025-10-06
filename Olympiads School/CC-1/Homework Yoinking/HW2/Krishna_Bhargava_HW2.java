import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Krishna_Bhargava_HW2 {

	
	public static int cycleLength(int s) {
		int cycleLength = 1;
		while (s !=1) {
			if (s % 2 == 0) {
				s = s/2;
			}
			else {
				s = s*3+1;
			}
			cycleLength++;
		}
		return cycleLength;
	}
	public static void main(String[] args) {	
		int k = 0;
		try {
			BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
			String line;
			while ((line = reader.readLine()) != null){
				k++;		
			}
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		String[][] strArray = new String[k][2];
		
		try {
			BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
			for (int m=0; m<k; m++){
				strArray[m] = reader.readLine().split(" ");
			}
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		int[][] intArray = new int[k][3];
		for( int i = 0; i<k; i++) {
			for(int j = 0; j<2;j++){
				intArray[i][j] = Integer.parseInt(strArray[i][j]);
			}
			int maxLength = 1;
			int currentLength = 1;
			for(int m = intArray[i][0]; m <= intArray[i][1]; m++) {
				currentLength = cycleLength(m);
				if(currentLength>maxLength ) {
					maxLength = currentLength;
				}
			
			}	
			intArray[i][2] = maxLength;
		}
		
		try {
			BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"));
			for (int i = 0; i<k; i++) {
				writer.write(Integer.toString(intArray[i][0])+" "+ Integer.toString(intArray[i][1])+" "+ Integer.toString(intArray[i][2]) + "\n");
			
			}
			writer.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}


