import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random random = new Random();

        List<Integer> nNumbers = new ArrayList<>();

        int i = scan.nextInt();
        int j = scan.nextInt();

        int n = random.nextInt(i) + j;

        while(true) {
            if (n % 2 == 0) {
                n = n / 2;
                nNumbers.add(n);
            } else{
                n = n * 3 + 1;
                nNumbers.add(n);
            }

            if(n == 1){
                break;
            }

        }

        System.out.println(i + " " + j + " " + nNumbers.size());

    }
}