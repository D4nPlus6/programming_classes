import java.util.Scanner;

public class kaley_wu_HW2 {
    public static int getCycle (int n){
        int count = 1;
        while(n!=1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = n * 3 + 1;
            }
         count++;
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner (System.in);
        int numInput = Integer.parseInt(s.nextLine());
        for (int i = 0; i < numInput; i++) {
            String [] inputs = s.nextLine().split(" ");
            int start = Integer.parseInt(inputs[0]);
            int end = Integer.parseInt(inputs[1]);
            int maxCount = 0;
            for (int j = start; j <=end ; j++) {
                int count = getCycle(j);
                if (count > maxCount){
                    maxCount = count;
                }
            }
            System.out.println(start + " " + end + " "+  maxCount);

        }
    }
}
